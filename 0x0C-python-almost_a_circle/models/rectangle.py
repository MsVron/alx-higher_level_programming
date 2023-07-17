#!/usr/bin/python3

"""Class representing a Rectangle."""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        x (int, optional): x coordinate of the rectangle. Defaults to 0.
        y (int, optional): y coordinate of the rectangle. Defaults to 0.
        id (int, optional): id of the rectangle. If not provided, an id is
            automatically assigned using the logic from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
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

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the rectangle."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x coordinate of the rectangle."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y coordinate of the rectangle."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height
    
    def display(self):
        """
        Print a visual representation of the rectangle using "#" character.
        """
        for i in range(self.height):
            print("#" * self.width)
