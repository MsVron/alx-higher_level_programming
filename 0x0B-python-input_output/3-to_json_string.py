#!/usr/bin/python3

"""
    Returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    :param my_obj: The object to be converted to JSON.
    :type my_obj: str
    :return: The JSON representation of the object.
    :rtype: str
    """
    return json.dumps(my_obj)
