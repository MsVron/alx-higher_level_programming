#!/usr/bin/python3

"""
A class representing a rectangle with BaseGeometry
"""


class Rectangle(BaseGeometry):

    """
    Initializes a Rectangle instance with the given width and height.
    """

    def __init__(self, width, height):
        """
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = None
        self.__height = None
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
