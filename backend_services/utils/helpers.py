from backend_services.services.models.user_model import User as UserModel
from backend_services.services.tables.user_table import (
    Contact,
    Education,
    Employment,
    PersonalInfo,
    Settings,
    Statistics,
    User,
)


def prepare_user_for_db(user: UserModel) -> User:
    personal_info = PersonalInfo(
        first_name=user.personal_info.first_name,
        last_name=user.personal_info.last_name,
        middle_name=user.personal_info.middle_name,
        birth_date=user.personal_info.birth_date,
        age=user.personal_info.age,
        gender=user.personal_info.gender,
    )

    contact = Contact(
        email=user.contact.email,
        phone=user.contact.phone,
        address=user.contact.address.model_dump(),
        networks=[network.model_dump() for network in user.contact.networks],
    )

    employment = Employment(
        position=user.employment.position,
        company=user.employment.company.model_dump(),
        experience=user.employment.experience,
        remote=user.employment.remote,
    )

    education = Education(
        level=user.education.level,
        institution=user.education.institution,
        faculty=user.education.faculty,
        graduation_year=user.education.graduation_year,
        degree=user.education.degree,
    )

    settings = Settings(
        is_active=user.settings.is_active,
        notifications=user.settings.notifications.model_dump(),
        privacy=user.settings.privacy.model_dump(),
    )

    statistics = Statistics(
        registration_date=user.statistics.registration_date,
        last_login=user.statistics.last_login,
        login_count=user.statistics.login_count,
        rating=user.statistics.rating,
    )

    db_user = User(
        personal_info=personal_info,
        contact=contact,
        employment=employment,
        education=education,
        settings=settings,
        statistics=statistics,
    )

    return db_user
