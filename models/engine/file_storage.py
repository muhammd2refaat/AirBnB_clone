#!/usr/bin/python3

import json
import os


class FileStorage:
    """serializes instances to a
    JSON file & deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serialize objects and save it to file_path"""
        ser = {}
        for key, obj in self.__objects.items():
            ser[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as fs:
            json.dump(ser, fs)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
