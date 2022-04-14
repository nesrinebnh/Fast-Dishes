from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)



class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(500))  # Many quotes to one author
    url = Column(String(255))
    image_url = Column(String(255))
    level= Column(String(50))
    duration = Column(Integer)

class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255))
