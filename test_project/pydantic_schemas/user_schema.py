from pydantic import BaseModel, EmailStr, Field


class UserDataSchema(BaseModel):
    id: str = Field(alias='_id')
    firstName: str
    lastName: str
    email: EmailStr
    version: int = Field(alias='__v')


class UserResponseSchema(BaseModel):
    user: UserDataSchema
    token: str


class UserProfileResponseSchema(BaseModel):
    id: str = Field(alias='_id')
    firstName: str
    lastName: str
    email: EmailStr
    version: int = Field(alias='__v')


class UserUpdateResponseSchema(BaseModel):
    id: str = Field(alias='_id')
    firstName: str
    lastName: str
    email: EmailStr
    version: int = Field(alias='__v')


class UserLogInSchema(BaseModel):
    id: str = Field(alias='_id')
    firstName: str
    lastName: str
    email: EmailStr
    version: int = Field(alias='__v')


class UserLogInResponseSchema(BaseModel):
    user: UserDataSchema
    token: str
