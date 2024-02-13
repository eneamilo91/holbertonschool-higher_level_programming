#!/usr/bin/python3

"""module for a class"""
import json


class Base:
    """class for some shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """func to convert to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        my_list = json.dumps(list_dictionaries)
        return my_list
