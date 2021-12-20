from fastapi import status, Depends, APIRouter
from fastapi.exceptions import HTTPException
from db import post_crud, db_connect
from models.schemas import PostResponseModel, PostRequestModel
from sqlalchemy.orm import Session
from typing import List


post_route = APIRouter(
    tags=["POST Endpoints"]
)


@post_route.get("/posts", response_model=List[PostResponseModel])
def get_post_all(db: Session = Depends(db_connect.get_db)):
    data = post_crud.get_posts(db)
    if data == []:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Posts Not Found")
    else:
        return data


@post_route.get("/posts/{id_}", response_model=PostResponseModel)
def get_post_id(id_: int, db: Session = Depends(db_connect.get_db)):
    data = post_crud.get_post_by_id(db, id_)
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    else:
        return data


@post_route.post("/posts", status_code=status.HTTP_201_CREATED)
def add_post(post: PostRequestModel, db: Session = Depends(db_connect.get_db)):
    data = post_crud.add_new_post(db, post)
    return data


@post_route.delete("/posts/{id_}")
def delete_post(id_: int, db: Session = Depends(db_connect.get_db)):
    delete_status = post_crud.delete_post_by_id(db, id_)
    if delete_status is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    return "post deleted"


@post_route.put("/posts/{id_}")
def update_post(id_: int, post_: PostRequestModel, db: Session = Depends(db_connect.get_db)):
    post_query = post_crud.update_post_by_id(db, id_)
    post = post_query.first()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    post_query.update(post_.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
