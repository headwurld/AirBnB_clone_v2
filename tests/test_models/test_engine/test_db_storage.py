#!/usr/bin/python3
""" Module for testing file storage"""
from io import StringIO
import os
import unittest
from console import HBNBCommand
from models import storage
from models.city import City
from models.state import State
from unittest.mock import patch, MagicMock


class TestDBStorage(unittest.TestCase):
    """ Test class for dbstorage """

    def __init__(self, *args, **kwargs):
        """ Test filestorage instantiation """
        super().__init__(*args, **kwargs)
        self.console = HBNBCommand()

    def setUp(self):
        """ Test set up """
        pass
    
    def tearDown(self):
        """Test removing json file or closing database connection"""
        pass

    @patch('models.engine.db_storage.DBStorage.all')
    def test_all_method(self, mock_all):
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            mock_all.return_value = {
                'State.1': State(id='1', name='California'),
                'City.1': City(id='1', name='Los Angeles', state_id='1')
            }

            all_objects = storage.all()

            self.assertIn('State.1', all_objects)
            self.assertIn('City.1', all_objects)
            self.assertIsInstance(all_objects['State.1'], State)
            self.assertIsInstance(all_objects['City.1'], City)

    @patch('models.engine.db_storage.DBStorage._DBStorage__session',
           new_callable=MagicMock)
    def test_new_method(self, mock_session):
        """Test the new() method"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            new_state = State(name="New York")
            storage.new(new_state)
            mock_session.add.assert_called_with(new_state)

    @patch('models.engine.db_storage.DBStorage._DBStorage__session',
           new_callable=MagicMock)
    def test_save_method(self, mock_session):
        """Test the save() method"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            new_state = State(name="Florida")
            storage.new(new_state)
            storage.save()
            mock_session.commit.assert_called_once()

    @patch('models.engine.db_storage.DBStorage._DBStorage__session',
           new_callable=MagicMock)
    def test_delete_method(self, mock_session):
        """Test the delete() method"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            state_to_delete = State(name="Texas")
            storage.new(state_to_delete)
            storage.delete(state_to_delete)
            mock_session.delete.assert_called_with(state_to_delete)

    @patch('models.storage', new_callable=MagicMock)
    def test_create_state_db_storage(self, mock_storage):
        """Test creating a state with the console using DBStorage"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("create State name=\"Louisiana\"")
                self.assertNotEqual(f.getvalue(), "** class doesn't exist **\n")
                self.assertNotEqual(f.getvalue(), "** class name missing **\n")
                mock_storage.new.assert_called()
                mock_storage.save.assert_called_once()
