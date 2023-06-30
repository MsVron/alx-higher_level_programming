#!/usr/bin/python3

"""
Import the math module for mathematical functions and constants
"""
import math


"""
This module provides a MagicClass for working with circles.
"""
"""
Define MagicClass
"""


class MagicClass:
    """
    A class representing a magic circle.

    Attributes:
        __radius (int or float): The radius of the circle.

    Methods:
        __init__(radius): Initialize a MagicClass instance with
        the given radius.
        area(): Calculate the area of the circle.
        circumference(): Calculate the circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance.

        Args:
            radius (int or float): The radius of the circle. (default: 0)

        Raises:
            TypeError: If the provided radius is not a number.
        """

        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """

        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """

        return 2 * math.pi * self.__radius
