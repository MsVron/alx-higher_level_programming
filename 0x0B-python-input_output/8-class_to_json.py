#!/usr/bin/python3

"""
Convert an instance of a class
into a dictionary representation suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation
        of the class object with serializable attributes.
    """
    json_dict = {}
    # Iterate over all attributes of the object
    for attr_name, attr_value in obj.__dict__.items():
        # Check if the attribute is serializable
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value

    return json_dict
