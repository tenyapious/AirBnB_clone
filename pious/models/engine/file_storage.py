#!/user/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User

''' Define the file storage '''

  
class FileStorage:
    ''' The FileStorage class '''

    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        objKey = obj.__class__.__name__ + '.' + obj.id
        self.__objects[objKey] = obj

    def save(self):
        obj_dict = {}

        if self.__objects is not None:
            for obj in self.__objects.keys():
                obj_dict[obj] = self.__objects[obj].to_dict()

            with open(self.__file_path, 'w', encoding="utf-8") as file:
                file.write(json.dumps(obj_dict))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_obj = json.loads(file.read())

            for obj in json_obj.values():
                className = obj["__class__"]
                del obj["__class__"]
                self.new(eval(className)(**obj))

