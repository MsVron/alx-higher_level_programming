#!/usr/bin/python3

"""
Writes an object to a text file using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    :param my_obj: The object to be serialized and saved to the file.
    :param filename: The name of the file to save the object.
    :type filename: str
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
