#!/usr/bin/python3
""" updating my dbstorage, create new class 
    for my sqlAlchemy Database
"""
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ create database table """
    __engine = None
    __session = None

    
    def __init__(self):
        """ Initialize DBStorage """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """ Query on the current database session all objects """

        obj_dict = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
        else:
            for cls in [State, City]
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    obj_dict[key] = obj
        return obj_dict


    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)


    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()


    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)


    def reload(self):
        """ Create all tables in the database and initialize a new session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()


    def close(self):
        """ Close the current session """
        if self.__session:
            self.__session.close()
