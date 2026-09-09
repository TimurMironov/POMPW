from backend_services.services.auth_service.auth_exceptions import IncorrectEmailOrPasswordError, UserAlreadyExistsError
from backend_services.services.auth_service.models.auth import Auth
from backend_services.services.auth_service.security import hash_password, verify_password
from backend_services.services.user_service.user_table import User


def register_user(db, user_data: Auth):
    user_db: User = db.query(User).filter(User.email == user_data.email).first()

    if user_db:
        raise UserAlreadyExistsError(f"User with email - {user_data.email} already exists")

    hashed_password = hash_password(user_data.password)
    user_db = User(
        email=user_data.email,
        hashed_password=hashed_password,
        is_active=True,
    )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db


def login_user(db, user_data: Auth):
    user_db: User = db.query(User).filter(User.email == user_data.email).first()

    if not user_db:
        raise IncorrectEmailOrPasswordError("Incorrect email or password")

    verified_password = verify_password(password=user_data.password, hashed_password=user_db.hashed_password)

    if not verified_password:
        raise IncorrectEmailOrPasswordError("Incorrect email or password")

    return user_db
