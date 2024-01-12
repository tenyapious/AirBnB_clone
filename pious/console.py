#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
