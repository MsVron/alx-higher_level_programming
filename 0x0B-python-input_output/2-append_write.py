#!/usr/bin/python3

"""
Appends a string at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    :param filename: The name of the file to append to (optional).
    :type filename: str
    :param text: The string to append to the file.
    :type text: str
    :return: The number of characters added to the file.
    :rtype: int
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_chars_added = file.write(text)
        return num_chars_added
