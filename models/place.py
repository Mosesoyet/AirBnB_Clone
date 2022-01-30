#!/usr/bin/python3
"""`Place` class that inherits from `BaseModel`
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Inherits from `BaseModel to create a place
    Attributes:
        city_id (str): To hold the `City.id`
        user_id (str): To hold the `User.id`
        name (str): To hold the place name
        description (str): To hold the description
        number_rooms (int): To hold number of rooms
        number_bathrooms (int): To hold number of bathrooms
        max_guest (int): To hold maximum number of guests
        price_by_night (int): To hold price by night
        latitude (float): To hold latitude value
        longitude (float): To hold value of longitude
        amenity_ids (list of strings): To hold the list of `Amenity.id`
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
