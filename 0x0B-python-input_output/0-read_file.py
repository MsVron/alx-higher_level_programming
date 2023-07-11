#!/usr/bin/python3

"""
Reads a text file and prints its contents to stdout.
"""


def read_file(filename=""):
    """
    :param filename: The name of the file to be read (optional).
    :type filename: str
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
