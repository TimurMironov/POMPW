from pydantic import BaseModel, EmailStr, ConfigDict, Field


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str

class Geo(BaseModel):
    lat: float
    lon: float

class UserModel(BaseModel):
    id: int
    name: str
    username: str
    email:EmailStr
    address: Address
    geo: Geo = Field(..., alias="geolocation")

    model_config = ConfigDict(
        populate_by_name=False,
    )

"""
    {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    }
"""
