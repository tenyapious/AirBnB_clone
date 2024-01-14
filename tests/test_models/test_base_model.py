#!/user/bin/python3
""" Define a test class TestBaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel

my_model = BaseModel()


class TestUUID(unittest.TestCase):
    """ Define TestUUID test class """

    def test_isnotnone(self):
        """ Assert id is not None """
        self.assertIsNotNone(my_model.id)

    def test_isstring(self):
        """ Assert id is a string """
        self.assertTrue(isinstance(my_model.id, str))


class TestCreatedAt(unittest.TestCase):
    """ Define TestCreatedAt test class """

    def test_isnotnone(self):
        """ Assert created_at is not None """
        self.assertIsNotNone(my_model.created_at)

    def test_isdatetime(self):
        """ Assert created_at is an instance of datetime """
        self.assertTrue(isinstance(my_model.created_at, datetime))


class TestUpdatedAt(unittest.TestCase):
    """ Define TestUpdatedAt test class """

    def test_isnotnone(self):
        """ Assert updated_at is not None """
        self.assertIsNotNone(my_model.updated_at)

    def test_isdatetime(self):
        """ Assert updated_at is a string """
        self.assertTrue(isinstance(my_model.updated_at, datetime))
