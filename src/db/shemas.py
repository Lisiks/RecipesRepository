from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Text, ForeignKey, PrimaryKeyConstraint


class Base(DeclarativeBase):
    ...


class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, unique=True)


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


