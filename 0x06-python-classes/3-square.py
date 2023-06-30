#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """
    A class representing a square shape.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square object with a given size.
        area(self): Calculates the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
