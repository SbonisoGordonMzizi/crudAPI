from fastapi import FastAPI
from db import post_crud, db_connect
from route import post_path, user_path


db_connect.Base.metadata.create_all(bind=db_connect.engine)


app = FastAPI(
    title="crudAPI  ",
    description="simple crudPI",
    version="0.0.1"
              )

app.include_router(post_path.post_route)
app.include_router(user_path.user_route)
