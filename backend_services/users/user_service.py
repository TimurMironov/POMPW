import json
from pathlib import Path

from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/users")
def user():
    users_path_json = Path(__file__).parent / "users.json"
    with open(users_path_json, 'r', encoding='utf-8') as file:
        response = json.load(file)
    return response
