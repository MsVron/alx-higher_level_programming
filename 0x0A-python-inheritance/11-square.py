#!/usr/bin/python3

"""Square class Module"""
Rectangle = __import__("9-rectangle").Rectangle

"""
A class representing a square.
"""


class Square(Rectangle):
    """
Initializes a Square instance with the given size.
    """

    def __init__(self, size):
        """
        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)
        self.__size = size

    """
    Returns a string representation of the square.
    """
    
    def __str__(self):
        """
        Returns:
            str: The string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
