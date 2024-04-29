from fastapi import FastAPI, HTTPException
from models import User, CharacterBuild
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://gsteere:!Beaumont11@host:5432/poe_build_manager"

app = FastAPI()

character_builds = []

@app.post("/builds/")
async def create_build(build: CharacterBuild):
    character_builds.append(build)
    return build

@app.get("/builds/")
async def get_build():
    return character_builds

@app.put("/builds/")
async def update_build(build: CharacterBuild):
    for i, existing_build in enumerate(character_builds):
        if existing_build.id == build.id:
            character_builds[i] = build
            return build
    raise HTTPException(status_code=404, detail="Build not found")

@app.delete("/builds/")
async def delete_build(id: int):
    for build in character_builds:
        if str(build.id) == str(id):
            character_builds.remove(build)
            return {"message": "Build deleted sucessfully"}
    raise HTTPException(status_code=404, detail="Build not found")




           