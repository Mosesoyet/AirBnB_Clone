#!/usr/bin/python3
"""
a class that contain the console command
"""

import cmd
from datetime import datetime
import shlex #For splitting the line along spaces except in double quotes

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
