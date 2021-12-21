from fastapi import status, Depends, APIRouter
from fastapi.exceptions import HTTPException
from db import user_crud, db_connect
from models.schemas import UserRequestModel, UserResponseModel
from sqlalchemy.orm import Session
from typing import List

user_route = APIRouter(
    tags=["USER Endpoints"]
)


@user_route.get("/users/id/{id_}", response_model=UserResponseModel)
def get_user_profile_by_id(id_: int, db: Session = Depends(db_connect.get_db)):
    data = user_crud.get_user_by_id(db,id_)
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    else:
        return data


@user_route.get("/users/email/{email}", response_model=UserResponseModel)
def get_user_profile_by_email(email: str, db: Session = Depends(db_connect.get_db)):
    data = user_crud.get_user_by_email(db, email)
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Posts Not Found")
    else:
        return data


@user_route.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserResponseModel)
def create_new_user(user: UserRequestModel, db: Session = Depends(db_connect.get_db)):
    data = user_crud.create_new_user(db, user)
    return data