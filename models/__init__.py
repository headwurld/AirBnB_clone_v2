#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
import os

HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
