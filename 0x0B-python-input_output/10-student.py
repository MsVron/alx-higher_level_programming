#!/usr/bin/python3

"""
Student class
"""


class Student:
    """
    Initialize a Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    Retrieve a dictionary representation of the Student instance.
    """
    def to_json(self, attrs=None):
        """
        Args:
            attrs (list, optional): List of attribute names to be retrieved.
                If None, retrieve all attributes. Defaults to None.

        Returns:
            dict: A dictionary representing the Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            attrs = set(attrs)

        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)

        return json_dict
