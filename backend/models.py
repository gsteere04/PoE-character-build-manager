from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str

class CharacterBuild(BaseModel):
    id: int
    name: str
    class_name: str
    level: int
    items_equiped: list[str]
    skill_gems_used: list[str]
    passive_tree: str
    notes: str


    