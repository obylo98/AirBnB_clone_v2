#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
<<<<<<< HEAD
import os


class test_Amenity(test_basemodel):
    """ amenity test class"""

    def __init__(self, *args, **kwargs):
        """inti the test class """
=======


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
<<<<<<< HEAD
        """testing name type """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
=======
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
>>>>>>> cbaedfdd56b6e339a0af634cae7c81972e647043
