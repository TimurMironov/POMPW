from backend_services.services.models.user_model import User as UserModel
from backend_services.services.tables.user_table import (
    Contact,
    Statistics,
    User,
)


def prepare_user_for_db(user: UserModel) -> User:
    contact = Contact(
        email=user.contact.email,
        phone=user.contact.phone,
        address=user.contact.address.model_dump(),
        networks=[network.model_dump() for network in user.contact.social_networks],
    )

    statistics = Statistics(
        registration_date=user.statistics.registration_date,
        last_login=user.statistics.last_login,
        login_count=user.statistics.login_count,
        rating=user.statistics.rating,
    )

    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
        birth_date=user.birth_date,
        age=user.age,
        gender=user.gender,
        nationality=user.nationality,
        contact=contact,
        statistics=statistics,
    )

    return db_user
