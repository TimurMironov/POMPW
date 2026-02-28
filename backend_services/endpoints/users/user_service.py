import json

from pathlib import Path as FilePath
from typing import Annotated

from fastapi import HTTPException, Path
from fastapi.routing import APIRouter

from backend_services.users.user_model import User

router = APIRouter()


@router.get("/users")
async def get_users():
    users_path_json = FilePath(__file__).parent / "users.json"
    with open(users_path_json, 'r', encoding='utf-8') as file:
        users_list = json.load(file)
    return users_list


@router.get("/users/{user_id}")
async def get_user(user_id: Annotated[int, Path(..., ge=1, title="ID пользователя")]) -> User:
    users_path_json = FilePath(__file__).parent / "users.json"
    with open(users_path_json, "r", encoding='utf-8') as file:
        users_list: list[dict] = json.load(file)
    for user in users_list:
        if user.get("id") == user_id:
            return User.model_validate(user)
    raise HTTPException(status_code=404, detail="User not Found")


@router.post("/users/add")
async def add_user(user: User):
    User.model_validate(user)
    users_path_json = FilePath(__file__).parent / "users.json"
    with open(users_path_json, "r", encoding='utf-8') as file:
        all_users: list = json.load(file)
    all_users.append(user)
    with open(users_path_json, 'w', encoding='utf-8') as file:
        json.dump(all_users, file, indent=4, ensure_ascii=False)
# Query() описывает то что идет после ? в url