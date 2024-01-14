#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Args:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_create(self, className):
        """ create command to create a new class object and print out the id.
        Usage: create <class>

        Args:
            className: The name of the class
        """
        if len(className) == 0:
            print("** class name missing **")
        else:
            try:
                my_model = globals()[className]()
                storage.save()
                print(my_model.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, className_objId):
        """ show command to show the string representation
        of a class object of a given id.
        Usage: show <class> <id>

        Args:
           className_objId(str): The object's class name and id
        """

        line_args = className_objId.split()
        if len(line_args) == 0:
            print("** class name missing **")
        elif len(line_args) == 1:
            print("** instance id missing **")
        else:
            arg_className, arg_id = [arg for arg in line_args]
            objects = storage.all()
            classNameFound = False
            idFound = False
            for key, value in objects.items():
                inst_className, inst_id = [val for val in key.split(".")]
                if arg_className == inst_className:
                    classNameFound = True
                    if arg_id == inst_id:
                        idFound = True
                        print(value.__str__())

            if classNameFound:
                if not idFound:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, className_objId):
        """ destroy command to delete a class object of a given id.
        Usage: destroy <class> <id>
        Args:
           className_objId(str): The object's class name and id
        """

        line_args = className_objId.split()
        if len(line_args) == 0:
            print("** class name missing **")
        elif len(line_args) == 1:
            print("** instance id missing **")
        else:
            arg_className, arg_id = [arg for arg in line_args]
            objects = storage.all()
            classNameFound = False
            idFound = False
            for key, value in objects.items():
                inst_className, inst_id = [val for val in key.split(".")]
                if arg_className == inst_className:
                    classNameFound = True
                    if arg_id == inst_id:
                        idFound = True
                        del_key = key

            if classNameFound:
                if idFound:
                    del objects[del_key]
                    storage.save()
                if not idFound:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, className=""):
        """ all command to show string representations
        of all object of a given class.
        Usage: all or all <class>

        Args:
           className(str): The object's class name
        """

        objects = storage.all()
        list_objects = []

        if objects:
            for obj_key, obj_val in objects.items():
                if not className or className == obj_val.__class__.__name__:
                    list_objects.append(str(obj_val))

        if className and len(list_objects) == 0:
            print("** class doesn't exist **")
        else:
            print(list_objects)

    def do_update(self, className_objId_attr_attr_val):
        """ update command to update the attribute of a class object.
        Usage: update <class> <id> <attribute_name> <attribute_value>

        Args:
           className_objId_attr_attr_val(str): The object's class name,
           id, attribute to update and attribute value
        """

        line_args = shlex.split(className_objId_attr_attr_val)
        if len(line_args) == 0:
            print("** class name missing **")
        elif len(line_args) == 1:
            print("** instance id missing **")
        elif len(line_args) == 2:
            print("** attribute name missing **")
        elif len(line_args) == 3:
            print("** value missing **")
        else:
            arg_className, arg_id, attr, attr_val = [arg for arg in line_args]
            objects = storage.all()
            classNameFound = False
            idFound = False
            for obj_key, obj_value in objects.items():
                inst_className, inst_id = [val for val in obj_key.split(".")]
                if arg_className == inst_className:
                    classNameFound = True
                    if arg_id == inst_id:
                        idFound = True

                        try:
                            attr_val = float(attr_val)
                            if attr_val.is_integer():
                                setattr(obj_value, str(attr), int(attr_val))
                            else:
                                setattr(obj_value, str(attr), attr_val)
                        except ValueError:
                            setattr(obj_value, str(attr), str(attr_val))

                        storage.save()

            if classNameFound:
                if not idFound:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_quit(self, line):
        """ Quit command to exit the program """

        return True

    def do_EOF(self, line):
        """ EOF signal to exit the program """

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
