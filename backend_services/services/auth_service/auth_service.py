from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend_services.db.database import get_db
from backend_services.services.auth_service.auth_exceptions import IncorrectEmailOrPasswordError, UserAlreadyExistsError
from backend_services.services.auth_service.auth_helper import login_user, register_user
from backend_services.services.auth_service.dependencies import get_current_user
from backend_services.services.auth_service.models.auth import Auth
from backend_services.services.auth_service.models.auth_response import AuthResponse
from backend_services.services.auth_service.models.register_response import RegisterResponse
from backend_services.services.auth_service.security import create_access_token
from backend_services.services.user_service.user_table import User as UserDB

router = APIRouter()


@router.post("/register", response_model=RegisterResponse)
async def register_new_user(user_data: Auth, session: Session = Depends(get_db)):
    try:
        user = register_user(db=session, user_data=user_data)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=409, detail=str(e)) from None
    return user


@router.post("/login", response_model=AuthResponse)
async def login_exist_user(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    user_data = Auth(email=form_data.username, password=form_data.password)
    try:
        user = login_user(db=session, user_data=user_data)
    except IncorrectEmailOrPasswordError as e:
        raise HTTPException(status_code=401, detail=str(e))
    access_token = create_access_token(user.id)
    return AuthResponse(access_token=access_token, token_type="bearer")


@router.get("/me")
async def get_me(user: UserDB = Depends(get_current_user)):
    return user
