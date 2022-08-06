from starlite import Starlite,Provide
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin
from controllers.user import UserController
import database.model as app_model
from database.middleware import get_db
from database.middleware import SQLAlchemySessionMiddleware
from database.base import engine,Base

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
#app_model.Base.metadata.create_all(bind=engine)

app = Starlite(route_handlers=[UserController],middleware=[SQLAlchemySessionMiddleware], 
                                on_startup=[init_models],
                                plugins=[SQLAlchemyPlugin()],
                                dependencies={"db": Provide(get_db)})