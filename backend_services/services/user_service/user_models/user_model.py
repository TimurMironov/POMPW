from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_serializer


class Address(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    city: str = Field(...)
    street: str = Field(...)
    house: int = Field(...)
    apartment: int = Field(...)
    postal_code: str = Field(..., alias="postalCode")


class SocialNetwork(BaseModel):
    name: str = Field(...)
    username: str = Field(...)


class Contact(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    phone: str = Field(...)
    address: Address = Field(...)
    social_networks: list[SocialNetwork] = Field(alias="networks")


class Statistics(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    registration_date: datetime = Field(..., alias="registrationDate")
    last_login: datetime = Field(..., alias="lastLogin")
    login_count: int = Field(..., alias="loginCount")
    rating: float = Field(..., alias="rating")

    @field_serializer("registration_date", "last_login")
    def datetime_serializer(self, dt: datetime) -> str:
        return dt.isoformat()


class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    id: int | None = None
    first_name: str = Field(..., alias="firstName", min_length=1)
    last_name: str = Field(..., alias="lastName")
    middle_name: str = Field(alias="middleName")
    birth_date: str = Field(alias="birthDate")
    age: int = Field(alias="age")
    gender: Literal["male", "female"] = Field(...)
    nationality: str = Field(alias="nationality", default="Not defined")
    email: EmailStr = Field(...)
    password: str = Field(...)
    is_active: bool = Field(...)

    contact: Contact = Field(..., alias="contact")
    statistics: Statistics = Field(..., alias="statistics")
