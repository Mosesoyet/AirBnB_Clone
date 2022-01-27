#/usr/bin/python3
"""
Initializing the model package
"""

from models.engine.file_storage import Filestorage

storage = Filestorage()
storage.reload()
