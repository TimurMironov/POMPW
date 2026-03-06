import json
from pathlib import Path

from sqlalchemy.orm import Session

from backend_services.services.models.user_model import User as UserSchema
from backend_services.services.tables.user_table import User, PersonalInfo, Contact, Employment, Education, Settings, Statistics


def fill_users_tables(session: Session):
    path = Path(__file__).parent / "users_db.json"
    with open(path, 'r', encoding='utf-8') as users:
        users_list = json.load(users)

    for user in users_list:
        validated_user = UserSchema.model_validate(user)

        personal_info = PersonalInfo(
            first_name=validated_user.personal_info.first_name,
            last_name=validated_user.personal_info.last_name,
            middle_name=validated_user.personal_info.middle_name,
            birth_date=validated_user.personal_info.birth_date,
            age=validated_user.personal_info.age
        )

        contact = Contact(
            email=validated_user.contact.email,
            phone=validated_user.contact.phone,
            address=validated_user.contact.address.model_dump(),
            networks=[network.model_dump() for network in validated_user.contact.networks]
        )

        employment = Employment(
            position=validated_user.employment.position,
            company=validated_user.employment.company.model_dump(),
            experience=validated_user.employment.experience,
            remote=validated_user.employment.remote
        )

        education = Education(
            level=validated_user.education.level,
            institution=validated_user.education.institution,
            faculty=validated_user.education.faculty,
            graduation_year=validated_user.education.graduation_year,
            degree=validated_user.education.degree
        )

        settings = Settings(
            is_active=validated_user.settings.is_active,
            notifications=validated_user.settings.notifications.model_dump(),
            privacy=validated_user.settings.privacy.model_dump()
        )

        statistics = Statistics(
            registration_date=validated_user.statistics.registration_date,
            last_login=validated_user.statistics.last_login,
            login_count=validated_user.statistics.login_count,
            rating=validated_user.statistics.rating
        )

        db_user = User(
            personal_info=personal_info,
            contact=contact,
            employment=employment,
            education=education,
            settings=settings,
            statistics=statistics
        )

        session.add(db_user)

    session.commit()