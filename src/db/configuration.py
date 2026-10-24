from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, Session


database_link = URL.create(
    drivername="sqlite",
    database="recipes.db"
)


engine = create_engine(
    url=database_link,
    echo=False
)


sessions = sessionmaker(
    bind=engine,
    class_=Session
)