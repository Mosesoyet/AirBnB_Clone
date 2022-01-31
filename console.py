#!/usr/bin/python3
"""
a class that contain the console command
"""

import cmd
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    """The HBNB console"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """implements End Of File"""
        print()
        return True

    def do_quite(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        """Does nothing on ENTER"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
