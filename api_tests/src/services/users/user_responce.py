from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from api_tests.src.services.users.user_model import Contact, Statistics


class UserResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    id: int | None = None
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    middle_name: str = Field(alias="middleName")
    birth_date: str = Field(alias="birthDate")
    age: int = Field(alias="age")
    gender: Literal["male", "female"] = Field(...)
    nationality: str = Field(alias="nationality", default="Not defined")
    email: EmailStr = Field(...)
    is_active: bool = Field(...)

    contact: Contact = Field(..., alias="contact")
    statistics: Statistics = Field(..., alias="statistics")
