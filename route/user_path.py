from fastapi import status, Depends, APIRouter
from fastapi.exceptions import HTTPException
from db import user_crud, db_connect
from models.schemas import UserRequestModel, UserResponseModel,UserDeactivateModel
from sqlalchemy.orm import Session
from typing import List

user_route = APIRouter(
    tags=["USER Endpoints"]
)


@user_route.get("/api/v1/users/id/{user_id}", response_model=UserResponseModel)
def get_user_profile_by_id(user_id: int, db: Session = Depends(db_connect.get_db)):
    data = user_crud.get_user_by_id(db,user_id)
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    else:
        return data


@user_route.get("/api/v1/users/email/{email}", response_model=UserResponseModel)
def get_user_profile_by_email(email: str, db: Session = Depends(db_connect.get_db)):
    data = user_crud.get_user_by_email(db, email)
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Posts Not Found")
    else:
        return data


@user_route.post("/api/v1/users", status_code=status.HTTP_201_CREATED, response_model=UserResponseModel)
def create_new_user(user: UserRequestModel, db: Session = Depends(db_connect.get_db)):
    data = user_crud.create_new_user(db, user)
    return data


@user_route.delete("/api/v1/users/email/{user_email}")
def delete_post_by_email(user_email: str, db: Session = Depends(db_connect.get_db)):
    delete_status = user_crud.delete_user_by_email(db, user_email)
    if delete_status is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    return "account be deleted"


@user_route.delete("/api/v1/users/id/{user_id}")
def delete_post_by_email(user_id: int, db: Session = Depends(db_connect.get_db)):
    delete_status = user_crud.delete_user_by_id(db, user_id)
    if delete_status is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User Not Found")
    return "account deleted"


@user_route.put("/api/v1/users/update/{id_}")
def update_user_profile(id_: int, post_: UserRequestModel, db: Session = Depends(db_connect.get_db)):
    post_query = user_crud.update_user_by_id(db, id_)
    post = post_query.first()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User Not Found")
    post_query.update(post_.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()


@user_route.put("/api/v1/users/deactivate/{id_}")
def user_account_deactivate(id_: int, post_: UserDeactivateModel, db: Session = Depends(db_connect.get_db)):
    post_query = user_crud.deactivate_user_by_id(db, id_)
    post = post_query.first()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User Not Found")
    post_query.update(post_.dict(), synchronize_session=False)
    db.commit()
    return post_query.first(), "User account has been deactivated"
