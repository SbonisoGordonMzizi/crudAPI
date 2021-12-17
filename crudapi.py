from fastapi import FastAPI
from pydantic import BaseModel

#schema modeling class
class Post(BaseModel):
    title: str
    content: str
    published_public: bool = True




