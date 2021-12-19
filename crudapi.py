from fastapi import FastAPI, status, Depends
from fastapi.exceptions import HTTPException
from db import crud, db_connect
from models.schemas import PostResponseModel, PostRequestModel
from sqlalchemy.orm import Session

db_connect.Base.metadata.create_all(bind=db_connect.engine)


app = FastAPI()


@app.get("/posts")
def get_post_all(db: Session = Depends(db_connect.get_db)):
    data = crud.get_posts(db)
    if data == []:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Posts Not Found")
    else:
        return data


@app.get("/posts/{id_}", response_model=PostResponseModel)
def get_post_id(id_: int, db: Session = Depends(db_connect.get_db)):
    data = crud.get_post_by_id(db, id_)
    if data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    else:
        return data


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def add_post(post: PostRequestModel, db: Session = Depends(db_connect.get_db)):
    data = crud.add_new_post(db, post)
    return data


@app.delete("/posts/{id_}")
def delete_post(id_: int, db: Session = Depends(db_connect.get_db)):
    delete_status = crud.delete_post_by_id(db, id_)
    if delete_status is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    return "post deleted"
