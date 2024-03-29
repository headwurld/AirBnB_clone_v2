#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest
from models.place import Place
from models.state import State
from console import HBNBCommand
from unittest.mock import MagicMock, patch
from models.engine.file_storage import FileStorage
from tests.test_models.test_base_model import test_basemodel


class test_console(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        self.console = HBNBCommand()

    @patch('builtins.print')
    def test_do_create_int(self, mock_print):
        try:
            HBNBCommand.do_create(self, "Place number_rooms=four")
        except ValueError:
            self.assertNotIsInstance(int, type(Place.number_rooms))

    @patch('builtins.print')
    def test_do_create_float(self, mock_print):
        try:
            HBNBCommand.do_create(self, "Place latitude=thirty")
        except ValueError:
            self.assertNotIsInstance(float, type(Place.latitude))

    @patch('builtins.print')
    @patch('models.storage', new_callable=MagicMock)
    def test_create_state_file_storage(self, mock_storage, mock_print):
        """Test creating a state with the console using FileStorage"""
        self.console.onecmd("create State name=\"California\"")
        mock_storage.new.assert_called()
        mock_storage.save.assert_called_once()


if __name__ == '__main__':
    unittest.main()
