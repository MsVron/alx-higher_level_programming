#!/usr/bin/python3

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
Adds all arguments to a Python list
and saves them to a file using JSON representation.
"""


def main():
    """
    The list is saved as a JSON representation
    in a file named "add_item.json".
    If the file doesn’t exist, it will be created.
    """

    filename = "add_item.json"

    try:
        # Load existing data from the file
        data = load_from_json_file(filename)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        data = []

    # Add all arguments to the list
    data.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(data, filename)

if __name__ == '__main__':
    main()
