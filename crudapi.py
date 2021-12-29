from fastapi import FastAPI
from db import post_crud, db_connect
from route import post_path, user_path,auth_path
from fastapi.middleware.cors import CORSMiddleware

db_connect.Base.metadata.create_all(bind=db_connect.engine)

app = FastAPI(
    title="crudAPI  ",
    description="simple crudAPI, Created by : Sboniso Gordon Mzizi",
    version="0.0.1"
              )


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_path.post_route)
app.include_router(user_path.user_route)
app.include_router(auth_path.user_login_route)
