from starlite import Starlite,Provide
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin
from controllers.user import UserController
from controllers.preunderwriting import PUnderwrintController
import database.model as app_model
from database.middleware import SQLAlchemySessionMiddleware,get_db
from database.base import engine,Base
from security.auth_middleware import JWTAuthenticationMiddleware
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
#app_model.Base.metadata.create_all(bind=engine)

app = Starlite(route_handlers=[UserController,PUnderwrintController],middleware=[SQLAlchemySessionMiddleware,JWTAuthenticationMiddleware], 
                                on_startup=[init_models],
                                plugins=[SQLAlchemyPlugin()],
                                dependencies={"db": Provide(get_db)})