from fastapi import UploadFile
from pydantic import BaseModel, Field, ConfigDict, model_validator
from typing import Annotated, Self
from .resipe_type_dto import RecipeTypeGetDTO
from .resipe_steps_dto import RecipeStepGetDTO
from .ingridients_dto import IngredientsGetDTO


class RecipeBaseDTO(BaseModel):
    name: str
    type_id: int

    model_config = ConfigDict(
        from_attributes=True
    )
    
class RecipePostDTO(RecipeBaseDTO):
    step_description_list: Annotated[list[str], Field(min_length=1)]
    step_image_list: Annotated[list[UploadFile], Field(min_length=1)]
    ingridients_list: Annotated[list[int], Field(min_length=1)]

    @model_validator(mode="after")
    def check_steps_lists_lengths(self) -> Self:
        if len(self.step_description_list) != len(self.step_image_list):
            raise ValueError("Lists length was incorrect!")
        return self


class RecipeGetDTO(RecipeBaseDTO):
    id: int
    type: RecipeTypeGetDTO
    steps: list[RecipeStepGetDTO]
    ingridients: list[IngredientsGetDTO]