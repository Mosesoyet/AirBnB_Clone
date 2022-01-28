#!/usr/bin/python3
"""
This is the parent class from which other classes will be generated
"""

import models
import uuid
from datetime import datetime

time = "%Y-%m-%d-%H-%m-%s"

class BaseModel:
    """An attempt to create the parent class"""
    def __init__(self, *args, **kwargs):
        """initializing the attributes"""
        if kwargs:
            for key, value in kwargs:
                if key not in '__class__':
                    setattr(self, key, value)

            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs['created_at;'], time)

            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time)

        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """returns a string"""
        return "{[:s]} {(:s)} {}".format(self.__class__.__name__, self.id, self.__dic__)

    def save(self):
        """change 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        self.storage.save()

    def __init__(self):
        """returns a new dictionary and converts 'created_at' and 'updated_at' to ISO string format"""
        new_dic = self.__dic__.copy()

        if 'created_at' in new_dic:
            new_dic['created_at'] = new_dic['created_at'].datetime.strftime(time)

        if 'updated_at' in new_dic:
            new_dic['updated_at'] = new_dic['updated_at'].datetime.strftime(time)

        new_dic['__class__'] = self.__class__.__name__

        return new_dic
