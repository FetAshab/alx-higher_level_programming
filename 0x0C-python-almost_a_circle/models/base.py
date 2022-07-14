#!/usr/bin/python3
"""
Definning a Base Model class.
"""
import json


class Base:
    """
    Represents the Base model.
    Argumments:
        __nb_objects (int): Is the number of instancied Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing a New Base.
        Argumments:
            id (int): Identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Write an JSON File & save objects.
        Argumments:
            lists_dictionaries (list): List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
