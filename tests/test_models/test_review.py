#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
<<<<<<< HEAD
import os


class test_review(test_basemodel):
    """ review test class"""

    def __init__(self, *args, **kwargs):
        """ review class init"""
=======


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
<<<<<<< HEAD
        """ testing review place_id attr"""
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """ testing review user_id attr"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_text(self):
        """ testing review text attr"""
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
=======
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
