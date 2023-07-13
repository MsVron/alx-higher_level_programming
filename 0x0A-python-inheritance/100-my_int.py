#!/usr/bin/python3

"""
A class representing a rebel integer.
"""


class MyInt(int):

    """
    Overrides the equality operator (==) and inverts its behavior.
    """

    def __eq__(self, other):
        """
        Args:
            other: The object to compare with.

        Returns:
            bool: True if the objects are not equal, False otherwise.
        """
        return not super().__eq__(other)

    """
    Overrides the inequality operator (!=) and inverts its behavior.
    """

    def __ne__(self, other):
        """
        Args:
            other: The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        return not super().__ne__(other)
