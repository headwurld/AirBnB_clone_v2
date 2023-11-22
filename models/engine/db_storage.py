#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in the DataBase

    Attributes:
        __engine: current sqlalchemy engine
        __session: current sqlalchemy session"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance"""
        # self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
        #                               format(getenv("HBNB_MYSQL_USER"),
        #                                      getenv("HBNB_MYSQL_PWD"),
        #                                      getenv("HBNB_MYSQL_HOST"),
        #                                      getenv("HBNB_MYSQL_DB")),
        #                               pool_pre_ping=True)
        # Just for testing
        self.__engine = create_engine('sqlite:///mydb.db',
                                      pool_pre_ping=True, echo=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        session = DBStorage.__session()
        results = {}

        if cls is None:
            classes = [BaseModel, Amenity, City, Place, Review, State, User]
        else:
            classes = [cls]

        for class_obj in classes:
            objects = session.query(class_obj).all()
            for obj in objects:
                results['{}.{}'.format(obj.__name__, obj.id)] = obj

        return result     
