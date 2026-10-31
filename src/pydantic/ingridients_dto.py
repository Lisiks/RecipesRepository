from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated
from .ingridients_types_dto import IngredientsTypeGetDTO


class IngredientsBaseDTO(BaseModel):
    type: Annotated[str, Field(max_length=30)]

    model_config = ConfigDict(
        from_attributes=True
    )


class IngredientsPostDTO(IngredientsBaseDTO):
    ...


class IngredientsGetDTO(IngredientsBaseDTO):
    id: int

