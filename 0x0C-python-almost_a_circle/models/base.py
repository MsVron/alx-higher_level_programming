#!/usr/bin/python3
"""Defines the core Base model for other shapes."""

import json
import csv
import turtle


class Base:
    """The foundational structure for other models in the 0x0C* project.

    Class Attributes:
        __nb_objects (int): Counter for the number of instances.

    Instance Attributes:
        id (int): Unique identifier for each instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructs a Base.

        Args:
            id (int, optional): Identifier for the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # JSON operations
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON format of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Creates a list of dictionaries from a JSON string.

        Args:
            json_string (str): A string in JSON format.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the list that json_string represents.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    # File operations
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of a list of objects to a file.

        Args:
            list_objs (list): A list of instances inherited from Base.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Creates a list of instances from a JSON file.

        Reads from <cls.__name__>.json.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instances of cls.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]

    # Dictionary operations
    @classmethod
    def create(cls, **dictionary):
        """Constructs an instance of cls with specific attributes.

        Args:
            **dictionary (dict): Dictionary of attribute values.
        """
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy
