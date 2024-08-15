from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class ContactSchema(BaseModel):
    id: str = Field(alias='_id')
    firstName: str
    lastName: str
    birthdate: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    street1: Optional[str] = None
    street2: Optional[str] = None
    city: Optional[str] = None
    stateProvince: Optional[str] = None
    postalCode: Optional[str] = None
    country: Optional[str] = None
    owner: str = Field(alias='_id')
    version: int = Field(alias='__v')
