#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
<<<<<<< HEAD
import os


class test_state(test_basemodel):
    """ states test class"""

    def __init__(self, *args, **kwargs):
        """ state test class init"""
=======


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
<<<<<<< HEAD
        """ testing state name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
=======
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
