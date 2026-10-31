from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, ForeignKey, PrimaryKeyConstraint, String, Table, Column



class Base(DeclarativeBase):
    ...



class IngredientsType(Base):
    __tablename__ = "ingredients_type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(30), unique=True)

    ingredients: Mapped[list["Ingredients"]] = relationship()




class Ingredients(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    type_id: Mapped[int] = mapped_column(Integer, ForeignKey("ingredients_type.id", name="ingredients_type_id_fk", ondelete="RESTRICT", onupdate="CASCADE"))



class IngredientsResipes(Base):
    __tablename__ = "ingredients_resipes"

    ingredients_id: Mapped[int] = mapped_column(Integer, ForeignKey("ingredients.id", name="ingredients_id_fk", ondelete="CASCADE", onupdate="CASCADE"))
    recipe_id: Mapped[int] = mapped_column(Integer, ForeignKey("recipe.id", name="recipe_id_fk", ondelete="CASCADE", onupdate="CASCADE"))

    ingredient: Mapped["Ingredients"] = relationship()

    __table_args__ = (
        PrimaryKeyConstraint("ingredients_id", "recipe_id", name="ingredients_resipes_pk"),
    )




class RecipeType(Base):
    __tablename__ = "recipe_type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(30), unique=True)




class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, unique=True)
    type_id: Mapped[int] = mapped_column(Integer, ForeignKey("recipe_type.id", name="recipe_type_id_fk", ondelete="RESTRICT", onupdate="CASCADE"))

    type: Mapped["RecipeType"] = relationship()
    steps: Mapped[list["RecipeStep"]] = relationship(cascade="all, delete-orphan")
    ingridients: Mapped[list["IngredientsResipes"]] = relationship(cascade="all, delete-orphan")



class RecipeStep(Base):
    __tablename__ = "recipe_step"

    recipe_id: Mapped[int] = mapped_column(Integer, ForeignKey("recipe.id", name="recipe_id_fk", onupdate="CASCADE", ondelete="CASCADE"))
    recipe_step_number: Mapped[int] = mapped_column(Integer)
    recipe_step_description: Mapped[str] = mapped_column(Text)
    recipe_step_static_image: Mapped[str] = mapped_column(Text)
    recipe_step_storage_image: Mapped[str] = mapped_column(Text)

    __table_args__ = (
        PrimaryKeyConstraint("recipe_id", "recipe_step_number", name="recipe_step_pk"),
    )


