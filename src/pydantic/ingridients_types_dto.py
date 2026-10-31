from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated
from .ingridients_dto import IngredientsGetDTO


class IngredientsTypeBaseDTO(BaseModel):
    name: Annotated[str, Field(max_length=30)]
    type_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


class IngredientsTypePostDTO(IngredientsTypeBaseDTO):
    ...


class IngredientsTypeGetDTO(IngredientsTypeBaseDTO):
    id: int
    ingredients: list[IngredientsGetDTO]

