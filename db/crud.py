from sqlalchemy.orm import Session
from . import db_models
from models import schemas


def get_post_by_id(db: Session, post_id: int):
    return db.query(db_models.DbPost).filter(db_models.DbPost.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.DbPost).offset(skip).limit(limit).all()


def add_new_post(db: Session, post: schemas.PostRequestModel):
    new_post = db_models.DbPost(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
