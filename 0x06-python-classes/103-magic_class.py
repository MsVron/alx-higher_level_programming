#!/usr/bin/python3

"""
This module provides a MagicClass for working with circles.
"""
import math

"""Define a class MagicClass."""


class MagicClass:
    def __init__(self, radius):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
