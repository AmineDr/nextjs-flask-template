from pydantic import BaseModel, validator


class Login(BaseModel):
    username: str
    password: str

    # You can do what ever you want you can use regex to validate your data
    # This is just an example
    @validator('username')
    def validate_username(cls, username):
        if username.__len__() > 3:
            return username

    @validator('password')
    def validate_password(cls, password):
        if password.__len__() > 8:
            return password
