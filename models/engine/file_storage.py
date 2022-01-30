#!/usr/bin/python3
"""
A class 'Filestorage' to serialize instances to JSON and deserialize instance to JSON
"""

import JSON
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import Users
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

classes = {'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
        'Place': Place, 'Review': Review, 'State': State, 'User': User}

class FileStorage:
    """class for serialization and deserialization"""
    __file_path = "file.json"
    '''the path to the json file'''
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__name + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: '__file_path)"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dic()
        with open('self.__file_path', 'W') as f:
            JSON.dump(json_obj, f)
