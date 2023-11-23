#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
<<<<<<< HEAD
import os


class test_City(test_basemodel):
    """ tests for city """

    def __init__(self, *args, **kwargs):
        """ init the test class"""
=======


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
<<<<<<< HEAD
        """ testing state_id type """
        new = self.value()
        self.assertEqual(type(new.state_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """ testing name type"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
=======
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
