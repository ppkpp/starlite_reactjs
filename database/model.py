from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

from database.base import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)