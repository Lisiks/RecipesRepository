from ..configuration import sessions_maker
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from ...pydantic.ingridients_types_dto import IngredientsTypeGetDTO, IngredientsTypePostDTO
from ..shemas import IngredientsType, Ingredients



class IngridientTypeRepo:
    def create(type_data: IngredientsTypePostDTO) -> None:
        with sessions_maker() as session:
            new_ingr_type = IngredientsType(**type_data.model_dump())
            session.add(new_ingr_type)
            session.commit()


    def delete(type_id: int) -> None:
        with sessions_maker() as session:
            ingr_type = session.get(IngredientsType, int)
            session.delete(ingr_type)
            session.commit()


    def get_all() -> list[IngredientsTypeGetDTO]:
        with sessions_maker() as session:
            stmt = select(IngredientsType).options(selectinload(Ingredients)).order_by(IngredientsType.type)
            result = session.scalars(stmt)
            return [IngredientsTypeGetDTO.model_validate(record) for record in result.all()]
            

    