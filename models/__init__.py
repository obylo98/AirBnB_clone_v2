#!/usr/bin/python3
<<<<<<< HEAD
"""This module instantiates an instance of the Storage will be used"""

from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

=======
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
storage.reload()
