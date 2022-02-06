#!/usr/bin/python3
"""
a class that contain the console command
"""

import cmd
from datetime import datetime
import shlex #For splitting the line along spaces except in double quotes
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class HBNBCommand(cmd.Cmd):
    """The HBNB console"""
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """implements End Of File."""
        print()
        return True

    def do_quit(self, arg):
        """Exits the program."""
        return True

    def emptyline(self):
        """Does nothing on ENTER"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
