#!/usr/bin/python3

"""
Writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    :param filename: The name of the file to write to (optional).
    :type filename: str
    :param text: The string to write to the file.
    :type text: str
    :return: The number of characters written to the file.
    :rtype: int
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
        return num_chars_written
