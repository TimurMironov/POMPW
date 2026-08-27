class Endpoints:
    USERS = "/users"

    @classmethod
    def get_users(cls) -> str:
        return cls.USERS

    @classmethod
    def get_user(cls, user_id: int) -> str:
        return f"{cls.USERS}/{user_id}"

    @classmethod
    def create_user(cls) -> str:
        return f"{cls.USERS}"

    @classmethod
    def delete_user(cls, user_id: int) -> str:
        return f"{cls.USERS}/{user_id}"

    @classmethod
    def get_by_email(cls, email: str) -> str:
        return f"{cls.USERS}/search?email={email}"
