#!/usr/bin/python3
"""
A class from you other classes will be ceated
"""
import models
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%s.%f"

class BaseModel:
    """A parent class"""
    def __init__(self, *args, *kwargs):
        """initializing attributes"""
        if kwargs:
            for key, value in kwargs:
                if key not in "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs['created_at'], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()


    def __str__(self):
        """string to return"""
        return "{[:s]} {(:s)} {}".format(self.__class__.__name__, self.id,
                self.__dic__)

    def save(self):
        """Update attribute 'updated' at with current datetime"""
        updated_at = datetime.now()
        models.storage.save()

    def to_dic(self):
        """return a new dictionary containing all key and value"""
        new_dic = self.__dic__.copy()

        if "created_at" in new_dic:
            new_dic['created_at'] = new_dic['created_at'].strftime(time)
        if 'updated_at' in new_dic:
            new_dic['updated_at'] = new_dic['updated_at'].strftime(time)
        new_dic['__class__'] = self.__class__.__name__
        return new_dic
        
