#!/usr/bin/python3

"""Class representing a Rectangle."""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int, optional): x coordinate of the rectangle. Defaults to 0.
        y (int, optional): y coordinate of the rectangle. Defaults to 0.
        id (int, optional): id of the rectangle. If not provided, an id is
            automatically assigned using the logic from the Base class.
    """

    """Initialize a new Rectangle instance."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x coordinate of the rectangle. Defaults to 0.
            y (int, optional): y coordinate of the rectangle. Defaults to 0.
            id (int, optional): id of the rectangle. If not provided, an id is
                automatically assigned using the logic from the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Get the width of the rectangle."""

    @property
    def width(self):
        return self.__width

    """Set the width of the rectangle."""

    @width.setter
    def width(self, width):

        self.__width = width

    """Get the height of the rectangle."""

    @property
    def height(self):
        return self.__height

    """Set the height of the rectangle."""

    @height.setter
    def height(self, height):
        self.__height = height

        """Get the x coordinate of the rectangle."""

    @property
    def x(self):
        return self.__x

    """Set the x coordinate of the rectangle."""

    @x.setter
    def x(self, x):
        self.__x = x

    """Get the y coordinate of the rectangle."""

    @property
    def y(self):
        return self.__y

    """Set the y coordinate of the rectangle."""

    @y.setter
    def y(self, y):
        self.__y = y
