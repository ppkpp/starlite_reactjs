from datetime import datetime, timedelta
from uuid import UUID

from jose import JWTError, jwt
from pydantic import BaseModel, UUID4
from starlite.exceptions import NotAuthorizedException

from config import settings

DEFAULT_TIME_DELTA = timedelta(days=1)

class Token(BaseModel):
    exp: datetime
    iat: datetime
    sub: UUID4


def decode_jwt_token(encoded_token: str) -> Token:
    try:
        payload = jwt.decode(token=encoded_token, key=settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        return Token(**payload)
    except JWTError as e:
        raise NotAuthorizedException("Invalid token") from e


def encode_jwt_token(user_id: UUID, expiration: timedelta = DEFAULT_TIME_DELTA) -> str:
    token = Token(
        exp=datetime.now() + expiration,
        iat=datetime.now(),
        sub=user_id,
    )
    return jwt.encode(token.dict(), settings.JWT_SECRET, algorithm=settings.ALGORITHM)