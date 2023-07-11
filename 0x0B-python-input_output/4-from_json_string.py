#!/usr/bin/python3

"""
Returns an object (Python data structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    :param my_str: The JSON string representing the object.
    :type my_str: str
    :return: The Python data structure represented by the JSON string.
    :rtype: object
    """
    return json.loads(my_str)
