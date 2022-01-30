#!/usr/bin/python3
"""`City` class that inherits from `BaseModel`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Inherits from `BaseModel to create a city
    Attributes:
        state_id (str): to hold the State.id
        name (str): to hold city name
    """
    state_id = ""
    name = ""
