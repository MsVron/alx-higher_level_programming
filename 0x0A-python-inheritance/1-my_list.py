#!/usr/bin/python3

"""
A custom list class that inherits from the built-in list class.
It includes a method to print the list in sorted (ascending) order.
"""


class MyList(list):
    """
    Public Methods:
        print_sorted: Prints the list, sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
