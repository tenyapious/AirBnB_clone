#!/user/bin/python3
""" Define the base model """
import uuid
from datetime import datetime
import json
import models


class BaseModel:
    ''' The BaseModel class '''

    def __init__(self, *args, **kwargs):
        """ Initializes class variables

        Args:
            args: arguments
            kwargs: key word arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns: The string representation of the instance """
        returnStr = "[" + self.__class__.__name__ + "] "
        returnStr += "(" + self.id + ") "
        returnStr += str(self.__dict__)
        return returnStr

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance """

        newDict = {}

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                newDict[key] = value.isoformat()
            else:
                newDict[key] = value

            newDict["__class__"] = self.__class__.__name__

        return newDict
