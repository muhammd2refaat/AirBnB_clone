#!/usr/bin/python3

import json
import os


class FileStorage:
    """serializes instances to a
    JSON file & deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.all()[key] = obj

    def save(self):
        """serialize objects and save it to file_path"""
        json_dict = {}
        for key, value in self.all().items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as fp:
            json.dump(json_dict, fp)

    def reload(self):
        try:
            with open(self.__file_path, "r") as fp:
                json_dict = json.load(fp)
        except FileNotFoundError:
            return
        for key, value in json_dict.items():
            self.all()[key] = self.create_object(value["__class__"])(**value)

