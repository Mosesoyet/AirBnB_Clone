#!/usr/bin/python3
"""
The `BaseModel class` that defines all common attributes/methods
for other classes
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Defines the common attributes/methods for other classes
    """

        id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of an instance of BaseModel
        """
        clsname = self.__class__.__name__
        return "{[:s]} {(:s)} {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute `updated_at`
        with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of `__dict__` of the instance.
        """
        converted = self.__dict__.copy()
        converted["created_at"] = self.created_at.isoformat()
        converted["updated_at"] = self.updated_at.isoformat()
        converted["__class__"] = self.__class__.__name__
        return (converted)
