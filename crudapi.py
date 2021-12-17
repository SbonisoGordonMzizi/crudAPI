from fastapi import FastAPI,status,Response
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

#schema modeling class
class Post(BaseModel):
    title: str
    content: str
    published_public: bool = True


app = FastAPI()

@app.get("/posts")
def get_post_all(response:Response):
    #sql
    data = None
    if data == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Posts Not Found")
    else:
        return data


@app.get("/posts/{id}")
def get_post_id(id:int):
    #sql
    data = None
    if data == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    else:
        return data




