from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import setting

db_user = setting.config_env.database_username
db_pass = setting.config_env.database_password
db_name = setting.config_env.database_name
db_url = setting.config_env.database_hostname

DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_url}/{db_name}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
