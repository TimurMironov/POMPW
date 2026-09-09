from typing import Annotated

from fastapi import Depends, HTTPException, Path, Query
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session, joinedload

from backend_services.db.database import get_db
from backend_services.services.user_service.user_models.user_model import User
from backend_services.services.user_service.user_models.user_response import UserResponse
from backend_services.services.user_service.user_table import User as UserDB
from backend_services.utils.helpers import prepare_user_for_db

router = APIRouter()


@router.get("/users/search", response_model=list[User])
async def get_user_by_email(
    email: Annotated[str, Query(..., description="Email для поиска")],
    session: Session = Depends(get_db),
) -> list[User]:
    users: list = session.query(UserDB).filter(UserDB.email == email).all()

    if not users:
        raise HTTPException(status_code=404, detail="User not Found")
    return users


@router.get("/users", response_model=list[UserResponse])
async def get_users(session: Session = Depends(get_db)):
    all_users = (
        session.query(UserDB)
        .options(
            joinedload(UserDB.contact),
            joinedload(UserDB.statistics),
        )
        .all()
    )
    return all_users


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: Annotated[int, Path(..., ge=1, title="ID пользователя")],
    session: Session = Depends(get_db),
) -> User:
    user = (
        session.query(UserDB)
        .options(
            joinedload(UserDB.contact),
            joinedload(UserDB.statistics),
        )
        .filter(UserDB.id == user_id)
        .first()
    )
    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")
    return user


@router.post("/users")
async def add_user(user: User, session: Session = Depends(get_db)):
    user_db = prepare_user_for_db(user)
    session.add(user_db)
    session.commit()

    return {
        "status": "success",
        "message": "User created successfully",
        "user_id": user_db.id,
    }


@router.delete("/users/{user_id}")
async def delete_user(
    user_id: Annotated[int, Path(..., ge=1, title="ID пользователя")],
    session: Session = Depends(get_db),
):
    user_db = session.query(UserDB).filter(UserDB.id == user_id).first()
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not Found")
    session.delete(user_db)
    session.commit()

    return {
        "status": "success",
        "message": "User deleted successfully",
    }


# Query() описывает то что идет после ? в url
