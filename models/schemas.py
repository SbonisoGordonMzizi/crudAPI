from pydantic import BaseModel
from typing import Optional


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
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "title": "What is FastAPI",
                "content": "FastAPI is a Framework for creating Fast APIs",
                "published": True
            }
        }
