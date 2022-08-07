from typing import Any, List
from starlite import Controller, Partial, get, post, put, patch, delete

from database.model import PreUnderwritingData
from database.schema import PreUnderDataSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy import delete as sql_del
from security.auth_dependency import authenticated_guard
class  PUnderwrintController(Controller):
    path = "/preUnderwritingData"

    @post()
    async def create_user(self, data: PreUnderDataSchema,db:AsyncSession) -> PreUnderDataSchema:
        new_record = data.dict()
        print(new_record)
        return data
        
