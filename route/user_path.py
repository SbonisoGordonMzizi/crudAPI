from fastapi import status, Depends, APIRouter
from fastapi.exceptions import HTTPException
from db import user_crud, db_connect
from models.schemas import UserRequestModel, UserResponseModel
from sqlalchemy.orm import Session
from typing import List

user_route = APIRouter(
    tags=["USER Endpoints"]
)


@user_route.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserResponseModel)
def add_post(user: UserRequestModel, db: Session = Depends(db_connect.get_db)):
    data = user_crud.create_new_user(db, user)
    return data