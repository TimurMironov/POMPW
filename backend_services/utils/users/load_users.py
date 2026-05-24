import json
from pathlib import Path

from sqlalchemy.orm import Session

from backend_services.services.models.user_model import User as UserSchema
from backend_services.utils.helpers import prepare_user_for_db


def fill_users_tables(session: Session):
    path = Path(__file__).parent / "users_db.json"
    with open(path, encoding="utf-8") as users:
        users_list = json.load(users)

    for user in users_list:
        validated_user = UserSchema.model_validate(user)
        db_user = prepare_user_for_db(validated_user)
        session.add(db_user)
    session.commit()
