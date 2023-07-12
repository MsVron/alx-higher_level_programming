#!/usr/bin/python3

"""
Returns a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Args:
        obj: The object to look up.

    Returns:
        A list containing the names of attributes and methods.

    """
    attributes = dir(obj)
    return attributes
