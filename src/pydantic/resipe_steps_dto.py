from pydantic import BaseModel, ConfigDict


class RecipeStepBaseDTO(BaseModel):
    recipe_step_number: int
    recipe_step_description: str
    recipe_step_static_image: str
    recipe_step_storage_image: str

    model_config = ConfigDict(
        from_attributes=True
    )


class RecipeStepPostDTO(RecipeStepBaseDTO):
    ...


class RecipeStepGetDTO(RecipeStepBaseDTO):
    recipe_id: int
