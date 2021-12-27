from db import user_crud, db_connect
from models.schemas import UserResponseModel,Token
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from fastapi import Depends, status, HTTPException,APIRouter
from utils import encrypt_decrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models import schemas


user_login_route = APIRouter(
    tags=["USER AUTH EndPoints"]
)

oauth_object = OAuth2PasswordBearer(tokenUrl="/api/v1/token")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def authenticate_user(username: str, password: str, db: Session = Depends(db_connect.get_db)):
    user = user_crud.get_user_by_email(db, username)
    if not user:
        return False
    if not encrypt_decrypt.verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": encoded_jwt, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth_object), db: Session = Depends(db_connect.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("email")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = user_crud.get_user_by_email(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def is_user_active(current_user: UserResponseModel = Depends(get_current_user)):
    if current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@user_login_route.post("/api/v1/token")
def user_auth(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db_connect.get_db)):
    data = user_crud.get_user_by_email(db, form_data.username)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not encrypt_decrypt.verify_password(form_data.password, data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    jwt_token = create_access_token({"id": data.id, "email": data.email})
    return jwt_token


