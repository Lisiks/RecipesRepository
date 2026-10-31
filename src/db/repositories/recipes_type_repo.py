from ..configuration import sessions_maker
from sqlalchemy import select

from ...pydantic.resipe_type_dto import RecipeTypePostDTO, RecipeTypeGetDTO
from ..shemas import RecipeType



class IngridientRepo:
    def create(type_data: RecipeTypePostDTO) -> None:
        with sessions_maker() as session:
            new_type = RecipeType(**type_data.model_dump())
            session.add(new_type)
            session.commit()


    def delete(recipe_type_id: int) -> None:
        with sessions_maker() as session:
            recipe_type = session.get(RecipeType, int)
            session.delete(recipe_type)
            session.commit()

    def get_all() -> list[RecipeTypeGetDTO]:
        with sessions_maker() as session:
            stmt = select(RecipeType).order_by(RecipeType.type)
            result = session.scalars(stmt)
            return [RecipeTypeGetDTO.model_validate(record) for record in result.all()]

            

    