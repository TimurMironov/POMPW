from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from backend_services.services.user_service.user_models.user_model import Contact, Statistics


class UserResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    id: int | None = None
    first_name: str | None = Field(..., alias="firstName", min_length=1)
    last_name: str | None = Field(..., alias="lastName")
    middle_name: str | None = Field(alias="middleName")
    birth_date: str | None = Field(alias="birthDate")
    age: int | None = Field(alias="age")
    gender: Literal["male", "female"] | None = Field(...)
    nationality: str | None = Field(alias="nationality", default="Not defined")
    email: EmailStr = Field(...)
    is_active: bool = Field(...)

    contact: Contact | None = Field(..., alias="contact")
    statistics: Statistics | None = Field(..., alias="statistics")
