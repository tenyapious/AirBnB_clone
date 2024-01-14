#!/usr/bin/python3

""" Define a test classes """
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

class TestNew:
    def test_settingnewobj(self):
        obj = my_model.to_dict()
        FileStorage.new(obj)

        
