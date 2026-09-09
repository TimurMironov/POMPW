from datetime import UTC, datetime, timedelta

import jwt
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash

from backend_services.base_app.settings import base_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(user_id: int):
    now = datetime.now(UTC)
    expire = now + timedelta(minutes=base_settings.jwt_access_token_expire_minutes)
    payload = {
        "sub": str(user_id),
        "exp": expire.timestamp(),
    }
    return jwt.encode(
        payload=payload,
        key=base_settings.jwt_secret_key,
        algorithm="HS256",
    )
