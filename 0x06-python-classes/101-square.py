#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a Square object with a given size and position.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
