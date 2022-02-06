#!/usr/bin/python3
"""
`User` class that inherits from `BaseModel`
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from `BaseModel to create a user
    Attributes:
        email (str): to hold email
        password (str): to hold password
        first_name (str): to hold name
        last_name (str): to hold name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize user"""
        super().__init__(*args, **kwargs)
