from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated
from .ingridients_types_dto import IngredientsTypeGetDTO


class RecipeTypeBaseDTO(BaseModel):
    type: Annotated[str, Field(max_length=30)]

    model_config = ConfigDict(
        from_attributes=True
    )


class RecipeTypePostDTO(RecipeTypeBaseDTO):
    ...


class RecipeTypeGetDTO(RecipeTypeBaseDTO):
    id: int
    type: IngredientsTypeGetDTO
