from typing import Any
from starlite import Request, HTTPRouteHandler, NotAuthorizedException
from database.model import User
from security.token import Token


def authenticated_guard(request: Request[User, Token], _: HTTPRouteHandler) -> None:
    user = request.user  
    auth = request.auth  
    if not user:
        raise NotAuthorizedException()
