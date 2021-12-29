from fastapi import status, Depends, APIRouter
from fastapi.exceptions import HTTPException
from db import post_crud, db_connect
from models.schemas import PostResponseModel, PostRequestModel
from sqlalchemy.orm import Session
from typing import List
from .auth_path import is_user_active
from models import schemas

post_route = APIRouter(
    tags=["POST"]
)


@post_route.get("/api/v1/posts", response_model=List[PostResponseModel])
def get_post_all(user_active: schemas.UserResponseModel = Depends(is_user_active), db: Session = Depends(db_connect.get_db)):
    data = post_crud.get_posts(db)
    if data == []:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Posts Not Found")
    else:
        return data


@post_route.get("/api/v1/posts/{id_}", response_model=PostResponseModel)
def get_post_by_id(id_: int, user_active: schemas.UserResponseModel = Depends(is_user_active), \
                   db: Session = Depends(db_connect.get_db)):
    data = post_crud.get_post_by_id(db, id_)
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    else:
        return data


@post_route.post("/api/v1/posts", status_code=status.HTTP_201_CREATED)
def add_new_post(post: PostRequestModel, user_active:  schemas.UserResponseModel = Depends(is_user_active), \
                 db: Session = Depends(db_connect.get_db)):
    post_dict = post.dict()
    post_dict["user_id"] = user_active.id
    data = post_crud.add_new_post(db, post_dict)
    return data


@post_route.delete("/api/v1/posts/{id_}")
def delete_post_by_id(id_: int, user_active: schemas.UserResponseModel = Depends(is_user_active), \
                      db: Session = Depends(db_connect.get_db)):
    post = post_crud.delete_post_by_id(db, id_)
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    if post.first().user_id != user_active.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="permission error")
    post.delete(synchronize_session=False)
    db.commit()
    return "post deleted"


@post_route.put("/api/v1/posts/{id_}")
def update_old_post(id_: int, post_: PostRequestModel, user_active: schemas.UserResponseModel = Depends(is_user_active), \
                    db: Session = Depends(db_connect.get_db)):
    post_query = post_crud.update_post_by_id(db, id_)
    post = post_query.first()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    if post.user_id != user_active.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="permission error")
    post_query.update(post_.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
