#!/usr/bin/python3

"""
    this is the test for the amenity model.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        this is the testing Amenity class
    """

    def test_Amenity_inheritence(self):
        """
            this tests that the Amenity class Inherits from BaseModel
        """        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """
            this test the Amenity class had name attribute.
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """
            this is test the Amenity class had name attribute's type.
        """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)
