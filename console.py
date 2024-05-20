#!/usr/bin/python3
""" this module contains the entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
import re as regularExpression
from datetime import datetime as TIME
import json
from models.base_model import BaseModel
from models import storage
import cmd
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = "(hbnb) "
    
    # classes = [
    #     "BaseModel", "User", "State",
    #     "City", "Amenity", "Place",
    #     "Review"
    # ]

    def do_quit(self, *arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program.")

    def do_EOF(self, *arg):
        """EOF signal to exit the program."""
        return True

    def help_EOF(self):
        """EOF signal to exit the program"""
        print("EOF signal to exit the program.")

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id."""
        from models.base_model import BaseModel
        if not arg:
            print("** class name missing **")
            return
        try:
            n_instance = eval(arg)()
            storage.save()
            print(n_instance.id)
        except Exception:
            print("** class doesn't exist **")
            
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        cls_name, instance_id = args[0], args[1]
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])
        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        cls_name, instance_id = args[0], args[1]
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()
        
    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = arg.split()
        objects = storage.all()

        if len(args) == 0:
            # No class name provided, print all instances
            print([str(obj) for obj in objects.values()])
        else:
            cls_name = args[0]
            if cls_name not in globals():
                print("** class doesn't exist **")
                return
            # Class name provided, print only instances of that class
            print([str(obj) for key, obj in objects.items() if key.startswith(cls_name)])
            
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        cls_name, instance_id, attr_name, attr_value = args[0], args[1], args[2], args[3]
        key = f"{cls_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        # Retrieve the instance
        instance = storage.all()[key]

        # Prevent updating certain attributes
        if attr_name in ["id", "created_at", "updated_at"]:
            print(f"** can't update {attr_name} **")
            return

        # Cast attribute value to the correct type
        attr_type = type(getattr(instance, attr_name, str))
        try:
            attr_value = attr_type(attr_value)
        except ValueError:
            print("** invalid value **")
            return

        # Update the attribute and save the instance
        setattr(instance, attr_name, attr_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
