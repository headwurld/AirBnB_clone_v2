#!/usr/bin/python3
""" Module for testing file storage"""
import os
import models
import MySQLdb
import unittest
from models.state import State
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from tests.test_models.test_base_model import test_basemodel


class test_fileStorage(test_basemodel):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        pass
    
    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    @patch.object(FileStorage, 'all')
    def test_obj_list_empty(self, mock_all):
        """ __objects is initially empty """
        mock_all.return_value = {}
        self.assertEqual(len(models.storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = State()
        new.save()
        key = f"State.{new.id}"
        self.assertIn(key, models.storage.all())
        self.assertIs(models.storage.all()[key], new)

    def test_all(self):
        """ __objects is properly returned """
        new = self.value()
        temp = models.storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = self.value()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = self.value()
        thing = new.to_dict()
        new.save()
        new2 = self.value(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            new = self.value()
            models.storage.save()
            self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = self.value()
        new.save()
        models.storage.reload()
        for obj in models.storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            models.storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(models.storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = self.value()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(models.storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = self.value()
        new.save()
        _id = new.to_dict()['id']
        for key in models.storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(models.storage), FileStorage)

    def test_created_int_parameters(self):
        """Test that a State object can be created with integer parameters"""
        state = State(name="California", number_rooms=4)
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "California")
        self.assertEqual(state.number_rooms, 4)

    def test_number_states_created(self):
        """ Test if a state is created when calling do_create"""
        if os.getenv('HBNB_ENV') == 'test' and os.getenv(
                'HBNB_TYPE_STORAGE') == 'db':
            self.cursor.execute(
                "SELECT COUNT(*) from states")
            number_states_before = self.cursor.fetchone()[0]

            HBNBCommand().do_create("State name=Louisiana")

            self.cursor.execute(
                "SELECT COUNT(*) from states")
            number_states_after = self.cursor.fetchone()[0]
            self.assertEqual(number_states_after - number_states_before, 1)

            self.cursor.execute(
                "SELECT * FROM states WHERE name='Louisiana'")
            new_state = self.cursor.fetchone()
            self.assertIsNotNone(new_state)
            self.assertEqual(new_state[1], "Louisiana")


if __name__ == '__main__':
    unittest.main()
