#!/usr/bin/python3
"""
    this defines class FileStorage Module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        this serializes instances to JSON file and deserializes to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            this returns the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        this sets new obj into __objects
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        this serializes the objects into JSON file
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
        this reload the file and deserializes JSON into __objects
        """

        try:
            with open(FileStorage.__file_path) as fd:
                objectdict = json.load(fd)
            for key in objectdict.values():
                class_name = key["__class__"]
                del key["__class__"]
                self.new(eval(class_name)(**key))
        except FileNotFoundError:
            return
