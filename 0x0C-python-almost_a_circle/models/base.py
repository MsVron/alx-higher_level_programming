#!/usr/bin/python3

"""Base class for managing id attribute in all future classes."""


import json


class Base:
    """Base class for managing id attribute in all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The id of the instance.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): The list of dictionaries to convert.

        Returns:
            str: The JSON string representation of the list of dictionaries.

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): The list of objects to save.

        """
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        if list_objs else []

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): The JSON string to convert.

        Returns:
            list: The list of dictionaries representing the JSON string.

        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class and update its attributes
        based on a dictionary.

        Args:
            dictionary (dict): The dictionary containing the attributes
            of the new instance.

        Returns:
            obj: The newly created instance with updated attributes.

        """
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: The list of instances loaded from the JSON file.

        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]
