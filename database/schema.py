from datetime import datetime,date
from uuid import UUID
from typing import List, Optional,Any
from pydantic import BaseModel,validator
from sqlalchemy.orm import Query


class UserSchema(BaseModel):
    id : int
    first_name : str
    last_name : str
    class Config:
        orm_mode = True

class UserCreateSchema(BaseModel):
    first_name : str
    last_name : str
    class Config:
        orm_mode = True