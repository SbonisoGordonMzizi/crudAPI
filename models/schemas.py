from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import  datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True


class PostRequestModel(PostBase):
    class Config:
        schema_extra = {
            "example": {
                "title": "What is FastAPI",
                "content": "FastAPI is a Framework for creating Fast APIs",
                "published": True
            }
        }


class PostResponseModel(PostBase):
    time_created: datetime
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "What is FastAPI",
                "content": "FastAPI is a Framework for creating Fast APIs",
                "published": True,
                "time_created": "2021-12-19T11:40:24.618287+02:00"
            }
        }


class UserBase(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr


class UserRequestModel(UserBase):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "firstName": "Sboniso",
                "lastName": "Mzizi",
                "email": "smzizi@gmail.com",
                "password": "#@!?W1L2"
            }
        }


class UserResponseModel(UserBase):
    id: int
    is_active: bool
    time_created: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 10,
                "firstName": "Sboniso",
                "lastName": "Mzizi",
                "email": "smzizi@gmail.com",
                "is_active": "true",
                "time_created": "2021-12-19T11:40:24.618287+02:00"
            }
        }


class UserDeactivateModel(BaseModel):
    is_active: bool
    schema_extra = {
        "example": {
            "is_active": "true",
        }
    }


class UserAuthModel(BaseModel):
    email: EmailStr
    password: str
    schema_extra = {
        "example": {
            "email": "smzizi@gmail.com",
            "password": "vice12345"
        }
    }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

