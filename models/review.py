#!/usr/bin/python3
"""`Review` class that inherits from `BaseModel`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from `BaseModel to create a review
    Attributes:
        place_id (str): To hold the `Place.id`
        user_id (str): To hold the `User.id`
        text (str): To hold some text
    """

    place_id = ""
    user_id = ""
    text = ""
