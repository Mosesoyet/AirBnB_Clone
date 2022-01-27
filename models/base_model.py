#!/usr/bin/python3
"""
A class from you other classes will be ceated
"""
import models
import uuid
from datetime import datetime

time = "%Y-%m-%d-%T-%H-%M-%s-%f"

class Basemodel:
    """A parent class"""
    def __init__(self, *args, *kwargs):
        """initializing attributes"""

    def __str__(self):
        """string to return"""
        return "{[:s]} {(:s)} {}".format(self.__class__.__name__, self.id,
                self.__to__dic)

    def save(self):
        """Update attribute 'updated' at with current datetime"""
        updated_at = datetime.now()
        
