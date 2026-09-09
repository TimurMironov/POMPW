from pydantic import BaseModel, EmailStr, Field


class Auth(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
