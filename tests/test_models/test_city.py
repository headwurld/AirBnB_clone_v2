#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City


@unittest.skip("For now")
class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skip("FileStorage")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skip("FileStorage")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
