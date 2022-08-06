from typing import cast, TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import HTTPConnection
from starlite import (
    AbstractAuthenticationMiddleware,
    AuthenticationResult,
    NotAuthorizedException,
)

from database.model import User
from security.token import decode_jwt_token

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine

API_KEY_HEADER = "X-API-KEY"


class JWTAuthenticationMiddleware(AbstractAuthenticationMiddleware):
    async def authenticate_request(self, request: HTTPConnection) -> AuthenticationResult:
 
        auth_header = request.headers.get(API_KEY_HEADER)
        if not auth_header:
            #raise NotAuthorizedException()
            return AuthenticationResult(user=None, auth="")

        token = decode_jwt_token(encoded_token=auth_header)

        engine = cast("AsyncEngine", request.app.state.postgres_connection)
        async with AsyncSession(engine) as async_session:
            async with async_session.begin():
                user = await async_session.execute(
                    select(User).where(User.id == token.sub)
                )
        if not user:
            #raise NotAuthorizedException()
            return AuthenticationResult(user=None, auth="")
        return AuthenticationResult(user=user, auth=token)