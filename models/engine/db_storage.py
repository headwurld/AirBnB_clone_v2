#!/usr/bin/python3
"""
New class DBStorage
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor of the DBStorage class.
        This method creates the database engine instance.
        and the SQLAlchemy session.
        """
        """
        Obtener las credenciales de la base
        de datos desde variables de entorno
        """
        mysql_user = os.environ.get("HBNB_MYSQL_USER")
        mysql_pwd = os.environ.get("HBNB_MYSQL_PWD")
        mysql_host = os.environ.get("HBNB_MYSQL_HOST", "localhost")
        mysql_db = os.environ.get("HBNB_MYSQL_DB")

        """cadena de conexión para SQLAlchemy"""
        db_url = f"mysql+mysqldb://{mysql_user}: {mysql_pwd}@{mysql_host}/" \
            {mysql_db}"

        """motor de base de datos"""
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        """
        miramos si estamos en un entorno de prueba
        y eliminar las tablas si es necesario
        """
        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

        self.reload()

    def all(self, cls=None):
        from models import State, City, User, Amenity, Place, Review

        classes = {
            'State': State,
            'City': City,
            'User': User,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        result = {}

        if cls is None:
            for cls_name, cls in classes.items():
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = "{}.{}".format(cls_name, obj.id)
                    result[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(cls.__name__, obj.id)
                result[key] = obj
        return result

    def new(self, obj):
        """
        Agrega el objeto a la sesión de la
        base de datos actual (self.__session).
        """
        self.__session.add(obj)

    def save(self):
        """
        Confirma todos los cambios de la sesión
        de la base de datos actual (self.__session).
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Elimina el objeto de la sesión de la base
        de datos actual (self.__session) si no es None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Recarga la base de datos:
        - Crea todas las tablas en la base de datos.
        - Crea la sesión actual de la base de datos
        (self.__session) a partir del motor (self.__engine).
        """
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()
