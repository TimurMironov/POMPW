from pydantic import BaseModel, EmailStr, Field


class RegisterResponse(BaseModel):
    id: int = Field(...)
    email: EmailStr = Field(...)
    is_active: bool = Field(...)
