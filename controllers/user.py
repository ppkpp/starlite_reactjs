from typing import Any, List
from starlite import Controller, Partial, get, post, put, patch, delete

from database.model import User
from database.schema import UserSchema,UserCreateSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy import delete as sql_del
class UserController(Controller):
    path = "/users"

    @post()
    async def create_user(self, data: UserCreateSchema,db:AsyncSession) -> UserSchema:
        new_user =  User(**data.dict())
        db.add(new_user)
        await db.commit()
        return new_user

    @get()
    async def list_users(self,db:AsyncSession) -> List[UserSchema]:
        q = select(User)
        result = await db.execute(q)
        return result.scalars().all()

    @put(path="/{user_id:int}")
    async def update_user(self, user_id: int, data: UserCreateSchema,db:AsyncSession) -> UserSchema:
        user_query = (update(User).where(User.id == user_id).values(first_name=data.first_name,last_name=data.last_name).execution_options(synchronize_session="fetch"))#
        result = await db.execute(user_query)
        await db.commit()
        return data

    @delete(path="/{user_id:int}")
    async def delete_user(self, user_id: int,db:AsyncSession) -> None:
        query = sql_del(User).where(User.id == user_id)#returning(User)
        result = await db.execute(query)
        await db.commit()
        return {"status":"Success"}
         
        

