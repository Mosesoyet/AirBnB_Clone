#!/usr/bin/python3
"""`Amaenity` class that inherits from `BaseModel`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Inherits from `BaseModel to create an amenity
    Attributes:
        name (str): to hold name of amenity
    """
    name = ""
