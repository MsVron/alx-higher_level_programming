#!/usr/bin/python3

"""Rectangle class Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""
A class representing a rectangle.
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
        self.__width = self.__height = None
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """
    Computes and returns the area of the rectangle.
    """

    def area(self):
        """
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    """
    Returns a string representation of the rectangle.
    """

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
