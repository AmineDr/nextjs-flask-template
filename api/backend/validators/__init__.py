from pydantic import BaseModel, validator


class Login(BaseModel):
    username: str
    password: str

    # Atnak do what ever you want you can use regex to validate your data
    @validator('username')
    def validate_username(cls, username):
        if username.__len__() > 3:
            return username

    @validator('password')
    def validate_password(cls, password):
        if password.__len__() > 8:
            return password
