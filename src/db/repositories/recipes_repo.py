from ..configuration import sessions_maker
from sqlalchemy import insert, select, func, and_
from sqlalchemy.orm import joinedload, selectinload

from ...pydantic.resipe_dto import RecipeGetDTO, RecipePostDTO
from ...pydantic.resipe_steps_dto import RecipeStepGetDTO, RecipeStepPostDTO
from ...pydantic.ingridients_dto import IngredientsGetDTO
from ...pydantic.recipe_search_dto import RecipeSearch
from ..shemas import Recipe, RecipeStep, IngredientsResipes, RecipeType, Ingredients



class RecipeRepo:
    def create(resipe_data: RecipePostDTO, step_list: list[RecipeStepPostDTO]) -> None:
        with sessions_maker() as session:
            new_recipe = Recipe(
                name=resipe_data.name,
                type_id=resipe_data.type_id,
                steps=[RecipeStep(**step.model_dump()) for step in step_list],
                ingridients=[IngredientsResipes(ingredient_id) for ingredient_id in resipe_data.ingridients_list]
            )
            session.add(new_recipe)
            session.commit()


    def delete(resipe_id: int) -> None:
        with sessions_maker() as session:
            resipe = session.get(Recipe, resipe_id)
            session.delete(resipe)
            session.commit()


    def get_all(search_params: RecipeSearch) -> list[RecipeGetDTO]:
        with sessions_maker() as session:
            if (search_params.resipe_type_id is None and search_params.ingredients_list_ids is None):
                stmt = select(Recipe).options(
                    joinedload(RecipeType), 
                    selectinload(RecipeStep), 
                    selectinload(IngredientsResipes).joinedload(Ingredients)
                ).order_by(Recipe.name)

            elif (search_params.resipe_type_id is not None and search_params.ingredients_list_ids is None):
                stmt = select(Recipe).options(
                    joinedload(RecipeType), 
                    selectinload(RecipeStep), 
                    selectinload(IngredientsResipes).joinedload(Ingredients)
                ).where(Recipe.type_id == search_params.resipe_type_id).order_by(Recipe.name)

            elif (search_params.resipe_type_id is None and search_params.ingredients_list_ids is not None):
                stmt = select(Recipe).options(
                    joinedload(RecipeType), 
                    selectinload(RecipeStep), 
                    selectinload(IngredientsResipes).joinedload(Ingredients)
                ).join(
                    IngredientsResipes
                ).where(
                    IngredientsResipes.ingredients_id.in_(search_params.ingredients_list_ids)
                ).group_by(
                    Recipe.id
                ).having(
                    func.count(func.distinct(IngredientsResipes.ingredients_id)) == len(search_params.ingredients_list_ids)
                ).order_by(Recipe.name)

            else:
                stmt = select(Recipe).options(
                    joinedload(RecipeType), 
                    selectinload(RecipeStep), 
                    selectinload(IngredientsResipes).joinedload(Ingredients)
                ).join(
                    IngredientsResipes
                ).where(
                    and_(
                        Recipe.type_id == search_params.resipe_type_id,
                        IngredientsResipes.ingredients_id.in_(search_params.ingredients_list_ids)
                    )
                ).group_by(
                    Recipe.id
                ).having(
                    func.count(func.distinct(IngredientsResipes.ingredients_id)) == len(search_params.ingredients_list_ids)
                )

            result = session.scalars(stmt)
            return [RecipeStepGetDTO(
                id=record.id,
                name=record.name,
                type_id=record.type_id,
                type=record.type,
                steps=record.steps,
                ingridients=[IngredientsGetDTO.model_validate(ingr_record.ingredient) for ingr_record in record.ingridients]

            ) for record in result.all()]


