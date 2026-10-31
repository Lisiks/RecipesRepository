from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker, Session


database_link = "postgresql+psycopg2://lisiks:lisiks@localhost:5432/recipes"

engine = create_engine(
    url=database_link,
    echo=False
)


sessions = sessionmaker(
    bind=engine,
    class_=Session
)



