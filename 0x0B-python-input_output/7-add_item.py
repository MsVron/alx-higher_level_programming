#!/usr/bin/python3

"""
Creates an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    :param filename: The name of the JSON file to load the object from.
    :type filename: str
    :return: The object created from the JSON file.
    :rtype: object
    """
    with open(filename, "r") as file:
        return json.load(file)
