from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

class CharacterBuild(Base):
    __tablename__ = 'Character_Builds'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    class_name = Column(String)
    level = Column(Integer)
    items_equiped = (String)
    skill_gems_used = Column(String)
    passive_tree = Column(String)
    notes = Column(String)
    