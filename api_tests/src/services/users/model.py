from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict, EmailStr


class PersonalInfo(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    middle_name: str = Field(alias="middleName")
    birth_date: str = Field(alias="birthDate")
    age: int = Field(alias="age")
    gender: str = Field(...)
    nationality: str = Field(alias="nationality", default="Not defined")


class Address(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    city: str = Field(...)
    street: str = Field(...)
    house: str = Field(...)
    apartment: str = Field(...)
    postal_code: str = Field(..., alias="postalCode")

class SocialNetwork(BaseModel):
    name: str = Field(...)
    username: str = Field(...)

class Contact(BaseModel):
    email: EmailStr = Field(...)
    phone: str = Field(...)
    address: Address = Field(...)
    network: list[SocialNetwork]


class Employment(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",
    )
    position: str = Field(...)
    company_name: str = Field(..., alias="company.name")
    company_industry: str = Field(..., alias="company.industry")
    company_website: str = Field(..., alias="company.website")
    experience: int = Field(...)
    remote: bool


class Sports(BaseModel):
    type: str
    frequency: str
    experience: int

class Interests(BaseModel):
    hobbies: list[str]
    sports: list[Sports]
    music: list[str]


class Education(BaseModel):
    level: str = Field(...)
    institution: str
    faculty: str
    graduation_year: int = Field(..., alias="graduationYear")
    degree: str


class Settings(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )

    isActive: bool = Field(...)
    notifications_email: bool = Field(..., alias="notifications.email")
    notifications_sms: bool = Field(..., alias="notifications.sms")
    notifications_push: bool = Field(..., alias="notifications.push")
    privacy_profileVisible: str = Field(..., alias="privacy.profileVisible")
    privacy_showLocation: bool = Field(..., alias="privacy.showLocation")
    privacy_showAge: bool = Field(..., alias="privacy.showAge")


class Statistics(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    registration_date: datetime = Field(..., alias="registrationDate")
    last_login: datetime = Field(..., alias="lastLogin")
    login_count: int = Field(..., alias="loginCount")
    rating: float = Field(..., alias="rating")


class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    id: int
    personal_info: PersonalInfo = Field(..., alias="personalInfo")
    contact: Contact = Field(..., alias="contact")
    employment: Employment = Field(..., alias="employment")
    interests: Interests = Field(..., alias="interests")
    education: Education = Field(..., alias="education")
    settings: Settings = Field(..., alias="settings")
    statistics: Statistics = Field(..., alias="statistics")