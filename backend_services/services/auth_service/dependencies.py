import jwt
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from backend_services.base_app.settings import base_settings
from backend_services.db.database import get_db
from backend_services.services.auth_service.security import oauth2_scheme
from backend_services.services.user_service.user_table import User as UserDB


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_db),
):
    try:
        payload = jwt.decode(jwt=token, key=base_settings.jwt_secret_key, algorithms=["HS256"])
    except jwt.exceptions.PyJWTError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )

    user_id = int(payload["sub"])
    user = session.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
        )
    return user
