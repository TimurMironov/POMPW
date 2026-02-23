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

    email: EmailStr = Field(...)
    phone: str = Field(...)
    address: Address = Field(...)
    networks: list[SocialNetwork] = Field(alias="socialNetworks")


class Company(BaseModel):
    name: str
    industry: str
    website: str

class Employment(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        extra="ignore",
    )
    position: str = Field(...)
    company: Company
    experience: int = Field(...)
    remote: bool

class Education(BaseModel):
    level: str = Field(...)
    institution: str
    faculty: str
    graduation_year: int = Field(..., alias="graduationYear")
    degree: str


class Notifications(BaseModel):
    email: bool
    sms: bool
    push: bool

class Privacy(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )

    profile_visible: str = Field(..., alias="profileVisible")
    show_location: bool = Field(..., alias="showLocation")
    show_age: bool = Field(..., alias="showAge")

class Settings(BaseModel):
    isActive: bool = Field(...)
    notifications: Notifications
    privacy: Privacy


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
    education: Education = Field(..., alias="education")
    settings: Settings = Field(..., alias="settings")
    statistics: Statistics = Field(..., alias="statistics")