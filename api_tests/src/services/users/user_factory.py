import random
from datetime import datetime
from typing import Any

from faker import Faker


class UserFactory:
    GENDERS = ["male", "female"]
    NATIONALITY = ["Русский", "Американец", "Немец", "Француз"]
    SOCIAL_NETWORKS = ["Telegram", "WhatsApp", "LinkedIn"]

    def create_user(self) -> dict[str, Any]:
        faker = Faker("ru_RU")
        birth_date = faker.date_of_birth(minimum_age=18, maximum_age=60)

        return {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "middle_name": faker.middle_name(),
            "birth_date": birth_date.isoformat(),
            "age": (datetime.now().date() - birth_date).days // 365,
            "gender": random.choice(self.GENDERS),
            "nationality": random.choice(self.NATIONALITY),
            "email": faker.email(),
            "password": faker.password(),
            "is_active": True,
            "contact": {
                "phone": faker.phone_number(),
                "address": {
                    "city": faker.city(),
                    "street": faker.street_name(),
                    "house": random.randint(1, 150),
                    "apartment": random.randint(1, 150),
                    "postal_code": faker.postcode(),
                },
                "social_networks": [
                    {
                        "name": random.choice(self.SOCIAL_NETWORKS),
                        "username": faker.user_name(),
                    },
                    {
                        "name": random.choice(self.SOCIAL_NETWORKS),
                        "username": faker.user_name(),
                    },
                ],
            },
            "statistics": {
                "registration_date": faker.date_time_this_year().isoformat(),
                "last_login": faker.date_time_this_month().isoformat(),
                "login_count": random.randint(1, 1000),
                "rating": round(random.uniform(1.0, 5.0), 1),
            },
        }
