from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel
from starlette import status

SECRET_KEY = "9d3640c25ff80a86e2b6828c2092fe7adb4ab4872f4d6ae3138ef48dc0e22cd0ff3f0b06288696fe6f4e7b6056a2f1b73534de93ce0d8deb795dd7cbe13c5a29467abe313d8fc64a3e5d2ebe58c4e0dcaf738acd78c5b2a01c759f5fbe76325e586354e9551689542c346c4c3ece0b491c0a6e3e8604338dafd41673f8344c8a51e904bb254f95aa02516cdfec41e1109f39f6317b64836601c97ed00b6431f64691bab7a65c304dc81c51d2de29fe7f44c752c539a8ac9894059e83354c0b6acee0abda502319d3584502ad55abf220591d4e6d658691107c4c269e6d4c4107b7b129fb08bf81c6e65dd89e4788d308e9aed73d0212b4b5aa4b6691d0cdc6b1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
security = HTTPBearer()

class Token(BaseModel):
    access_token: str
    token_type: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login/")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        identification = payload.get("sub")

        if identification is None:
            raise credentials_exception
        return HTTPException(status_code=status.HTTP_200_OK, detail={"user_id": identification})
    except InvalidTokenError:
        raise credentials_exception

def get_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Извлекает Bearer токен из заголовка Authorization"""
    if credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=403, detail="Invalid authentication scheme")
    return credentials.credentials
