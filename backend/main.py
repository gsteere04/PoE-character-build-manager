from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


import schemas
import crud
SQLALCHEMY_DATABASE_URL = "postgresql://gsteere:postgres@host:5432/poe_build_manager"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()

character_builds = []

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{user_name}", response_model=schemas.User)
async def read_user(user_name: str, db: Session=Depends(get_db)):
    db_user = crud.get_user(db, user_name=user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.User, db: Session=Depends(get_db)):
    return crud.create_user(db=db, user=user)


















#@app.post("/builds/")
#async def create_build(build: schemas.CharacterBuild):
#    if build.name in character_builds:
#        raise HTTPException(status_code=403, detail="Character name already taken.")
#    else:
#        character_builds.append(build)
#    return build
#
#@app.get("/builds/")
#async def get_build():
#    return character_builds
#
#async def update_build(build: schemas.CharacterBuild):
#    for i, existing_build in enumerate(character_builds):
#        if existing_build.id == build.id:
#            character_builds[i] = build
#            return build
#    raise HTTPException(status_code=404, detail="Build not found")
#
#@app.delete("/builds/")
#async def delete_build(name: str):
#    for build in character_builds:
#        if str(build.name) == str(name):
#            character_builds.remove(build)
#            return {"message": "Build deleted sucessfully"}
#    raise HTTPException(status_code=404, detail="Build not found")





           