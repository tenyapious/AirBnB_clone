#!/user/bin/python3
""" Defines the FileStorage class """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ The FileStorage class """

    def __init__(self):
        """ Initialize the private attributes """

        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """ Returns:
                All created objects
        """
        return self.__objects

    def new(self, obj):
        """ Add new object to the dictionary object

        Args:
            obj (dict): The new object
        """
        objKey = obj.__class__.__name__ + '.' + obj.id
        self.__objects[objKey] = obj

    def save(self):
        """ Serializes and save `__objects` to the file named `__file_path` """

        obj_dict = {}

        if self.__objects is not None:
            for obj in self.__objects.keys():
                obj_dict[obj] = self.__objects[obj].to_dict()

            with open(self.__file_path, 'w', encoding="utf-8") as file:
                file.write(json.dumps(obj_dict))

    def reload(self):
        """ Deserializes `__file_path` contents and assign to `__objects` """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_obj = json.loads(file.read())

            for obj in json_obj.values():
                className = obj["__class__"]
                del obj["__class__"]
                self.new(eval(className)(**obj))
