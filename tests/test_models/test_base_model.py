#!/user/bin/python3


""" Define a test class TestBaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel

my_model = BaseModel()

class TestUUID(unittest.TestCase):
    def test_isnotnone(self):
        self.assertIsNotNone(my_model.id) 

    def test_isstring(self):
        self.assertTrue(isinstance(my_model.id, str))

class TestCreatedAt(unittest.TestCase):
    def test_isnotnone(self):
        self.assertIsNotNone(my_model.created_at) 

    def test_isdatetime(self):
        self.assertTrue(isinstance(my_model.created_at, datetime))

class TestUpdatedAt(unittest.TestCase):
    def test_isnotnone(self):
        self.assertIsNotNone(my_model.updated_at) 

    def test_isdatetime(self):
        self.assertTrue(isinstance(my_model.updated_at, datetime))
