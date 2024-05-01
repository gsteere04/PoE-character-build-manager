from sqlalchemy.orm import Session
import models
import schemas

def get_user(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.username == user_name).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.User):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_name: str, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.username == user_name).first()
    for key, value in user.model_dump().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_name: str):
    db_user = db.query(models.User).filter(models.User.username == user_name).delete()
    db.commit
    db.refresh(db_user)
    return (db_user)


def get_build(db: Session, character_id: int):
    return db.query(models.CharacterBuild).filter(models.CharacterBuild.id == character_id).first()

def get_builds(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.CharacterBuild).offset(skip).limit(limit).all()

def create_build(db: Session, build: schemas.CharacterBuild):
    db_build = models.CharacterBuild(**build.model_dump())
    db.add(db_build)
    db.commit()
    db.refresh(db_build)
    return db_build

def update_build(db: Session, build_id: int, build: schemas.CharacterBuild):
    db_build = db.query(models.CharacterBuild).filter(models.CharacterBuild.id == build_id).first()
    for key, value in build.model_dump().items():
        setattr(db_build, key, value)
    db.commit()
    return db_build

def delete_build(db: Session, build_name: str):
    db_build = db.query(models.CharacterBuild).filter(models.CharacterBuild.name == build_name).delete()
    db.commit()
    db.refresh(db_build)
    return db_build





