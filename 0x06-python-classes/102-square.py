#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0):
            Initializes a Square object with a given size.
        area(self):
            Calculates the area of the square.
        __eq__(self, other):
            Checks if two squares are equal in area.
        __ne__(self, other):
            Checks if two squares are not equal in area.
        __gt__(self, other):
            Checks if the area of the current square is greater than the area of another square.
        __ge__(self, other):
            Checks if the area of the current square is greater than or equal to the area of another square.
        __lt__(self, other):
            Checks if the area of the current square is less than the area of another square.
        __le__(self, other):
            Checks if the area of the current square is less than or equal to the area of another square.

    """

    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Check if two squares are equal in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal in area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        Check if two squares are not equal in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal in area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Check if the area of the current square is greater than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater than the other square in area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Check if the area of the current square is greater than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater than or equal to the other square in area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Check if the area of the current square is less than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is less than the other square in area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Check if the area of the current square is less than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is less than or equal to the other square in area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
