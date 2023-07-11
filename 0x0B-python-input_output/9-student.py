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
    def to_json(self):
        """

        Returns:
            dict: A dictionary representing the Student instance.
        """
        json_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return json_dict
