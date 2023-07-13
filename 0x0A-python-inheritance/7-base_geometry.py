#!/usr/bin/python3

"""
A base class for geometry-related operations and concepts.
"""


class BaseGeometry:
    """
    Computes the area of the geometry.
    """

    def area(self):
        """
        Raises:
            Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    """
    Validates the given value as an integer.
    """
    
    def integer_validator(self, name, value):
        """
        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: Indicates that the value is not an integer.
            ValueError: Indicates that the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
