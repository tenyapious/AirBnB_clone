#!/user/bin/python3
import uuid
from datetime import datetime
import json
import os

''' Define the file storage '''

  
class FileStorage:
    ''' The FileStorage class '''

    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        objKey = obj['__class__'] + '.' + obj['id']
        self.__objects[objKey] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            if self.__objects is not None:
                file.write(json.dumps(self.__objects))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_obj = file.read()

            self.__objects = json.loads(json_obj) 
