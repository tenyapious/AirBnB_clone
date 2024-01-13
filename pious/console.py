#!/usr/bin/python3

import cmd
import shlex

from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "

    def do_create(self, className):
        if len(className) == 0:
            print("** class name missing **")
        elif className == 'BaseModel':
            my_model = BaseModel()
            storage.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        line_args = line.split()
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

    def do_destroy(self, line):
        line_args = line.split()
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

    def do_all(self, class_name=""):
        objects = storage.all()
        list_objects = []

        if objects:
            for obj_key, obj_val in objects.items():
                if not class_name or class_name == obj_val.__class__.__name__:
                    list_objects.append(str(obj_val))

        if class_name and len(list_objects) == 0:
            print("** class doesn't exist **")
        else:
            print(list_objects)

    def do_update(self, line):
        line_args = shlex.split(line)
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
            print(attr_val)
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
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
