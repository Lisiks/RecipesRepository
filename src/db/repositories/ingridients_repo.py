from ..configuration import sessions_maker

from ...pydantic.ingridients_dto import IngredientsPostDTO
from ..shemas import Ingredients



class IngridientRepo:
    def create(type_data: IngredientsPostDTO) -> None:
        with sessions_maker() as session:
            new_ingredient = Ingredients(**type_data.model_dump())
            session.add(new_ingredient)
            session.commit()


    def delete(ingredient_id: int) -> None:
        with sessions_maker() as session:
            ingredient = session.get(Ingredients, int)
            session.delete(ingredient)
            session.commit()

            

    