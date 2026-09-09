from pydantic import BaseModel, Field


class AuthResponse(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(...)
