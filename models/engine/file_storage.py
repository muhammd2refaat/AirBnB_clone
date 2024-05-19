#!/usr/bin/python3

"""This module defines a class to manage file storage for hbnb clone"""
import json
# from os.path import isfile
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path for the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}

        for key, value in FileStorage.__objects.items():
            json_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(json_objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            deserialized = {}
            with open(FileStorage.__file_path) as f:
                deserialized = json.loads(f.read())
            FileStorage.__objects = {
                key: eval(value["__class__"])(**value)
                for key, value in deserialized.items()
            }
        except FileNotFoundError:
            pass
        except Exception as error:
            raise error
