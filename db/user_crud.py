from sqlalchemy.orm import Session
from . import db_models
from models import schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(db_models.DbUser).filter(db_models.DbUser.id == user_id).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(db_models.DbUser).filter(db_models.DbUser.email == user_email).first()


def create_new_user(db: Session, user: schemas.UserRequestModel):
    new_user = db_models.DbUser(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete_user_by_email(db: Session, user_email: str):
    user = db.query(db_models.DbUser).filter(db_models.DbUser.email == user_email)
    if user.first() is None:
        return None
    user.delete(synchronize_session=False)
    db.commit()
    return 1


def delete_user_by_id(db: Session, user_id: int):
    user = db.query(db_models.DbUser).filter(db_models.DbUser.id == user_id)
    if user.first() is None:
        return None
    user.delete(synchronize_session=False)
    db.commit()
    return 1


def update_user_by_id(db: Session, user_id: int):
    return db.query(db_models.DbUser).filter(db_models.DbUser.id == user_id)

