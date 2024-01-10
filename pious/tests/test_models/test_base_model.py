#!/user/bin/python3


""" Define a test class TestBaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestUUID(unittest.TestCase):

    def test_isstring(self):
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model.id, str))

class TestCreatedAt(unittest.TestCase):

    def test_isdatetime(self):
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model.created_at, datetime))

class TestUpdatedAt(unittest.TestCase):

    def test_isdatetime(self):
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model.updated_at, datetime))
