from .db_connect import Base
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql.expression import text


class DbPost(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    time_created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, server_default='TRUE', nullable=False)
    time_created = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
