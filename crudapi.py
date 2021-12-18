from fastapi import FastAPI, status, Response
from fastapi.exceptions import HTTPException
from db.db_connect import Base, engine, SessionLocal
from db.db_models import DbPost
from models.schemas import PostResponseModel, PostRequestModel


Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/posts")
def get_post_all(response: Response):
    #sql
    data = None
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Posts Not Found")
    else:
        return data


@app.get("/posts/{id}")
def get_post_id(id_: int):
    #sql
    data = None
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    else:
        return data




