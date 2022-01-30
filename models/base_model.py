#!/usr/bin/python3
"""
The `BaseModel class` that defines all common attributes/methods
for other classes
"""

import uuid
from datetime import datetime


class BaseModel:
    """Class for base model"""
    def __init__(self, *args, **kwargs):
        """Initializing of instances"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string which is readable to human"""
        return "{[:s]} {(:s)} {}".\
                format(type(self).__name__, self.id, self.__dic__)

    def save(self):
        """updates the updated at attribute with
        current datetime"""
        update_at = datetime.now()

    def to_dic(self):
        """returns a dictionary representation of an instance"""
        new_dic = self.__dic__.copy()
        new_dic['__class__'] = type(self).__name___
        new_dic['created_at'] = new_dic['created_at'].isoformat()
        new_dic['updated_at'] = new_dic['updated_at'].isoformat()
        return new_dic
