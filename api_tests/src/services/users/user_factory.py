import random
from datetime import datetime

from faker import Faker


class UserFactory:
    GENDERS = ["male", "female"]
    NATIONALITY = ["Русский", "Американец", "Немец", "Француз"]
    SOCIAL_NETWORKS = ["Telegram", "WhatsApp", "LinkedIn"]

    def create_user(self):
        faker = Faker("ru_RU")
        birth_date = faker.date_of_birth(minimum_age=18, maximum_age=60)

        return {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "middleName": faker.middle_name(),
            "birthDate": birth_date.isoformat(),
            "age": (datetime.now().date() - birth_date).days // 365,
            "gender": random.choice(self.GENDERS),
            "nationality": random.choice(self.NATIONALITY),
            "contact": {
                "email": faker.email(),
                "phone": faker.phone_number(),
                "address": {
                    "city": faker.city(),
                    "street": faker.street_name(),
                    "house": random.randint(1, 150),
                    "apartment": random.randint(1, 150),
                    "postalCode": faker.postcode(),
                },
                "socialNetworks": [
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
                "registrationDate": faker.date_time_this_year().isoformat(),
                "lastLogin": faker.date_time_this_month().isoformat(),
                "loginCount": random.randint(1, 1000),
                "rating": round(random.uniform(1.0, 5.0), 1),
            },
        }
