#!/usr/bin/python3
"""`State` class that inherits from `BaseModel`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Inherits from `BaseModel to create a state
    Attributes:
        name (str): to hold state name
    """

    name = ""
