from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class RecipeSearch(BaseModel):
    resipe_type_id: Optional[int] = None
    ingredients_list_ids: Optional[list[int]] = None