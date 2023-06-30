#!/usr/bin/python3

import math

"""
This module provides a MagicClass for working with circles.
"""

class MagicClass:
    """
    A class representing a magic circle.

    Attributes:
        __radius (int or float): The radius of the circle.

    Methods:
        __init__(radius): Initialize a MagicClass instance with the given radius.
        area(): Calculate the area of the circle.
        circumference(): Calculate the circumference of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a MagicClass instance.

        Args:
            radius (int or float): The radius of the circle.
        
        Raises:
            TypeError: If the provided radius is not a number.
        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """

        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """

        return 2 * math.pi * self.__radius
