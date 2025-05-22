from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
ENGIN = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

