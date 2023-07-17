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
        """
        Getter for width.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Setter for width.
        """
        self.__width = width

    @property
    def height(self):
        """
        Getter for height.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter for height.
        """
        self.__height = height

    @property
    def x(self):
        """
        Getter for x.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter for x.
        """
        self.__x = x

    @property
    def y(self):
        """
        Getter for y.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Setter for y.
        """
        self.__y = y

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character '#'.
        It takes into account the x and y attributes for printing.
        """
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def __str__(self):
        """
        Returns the print() and str() representation of the Rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y,
                        self.width, self.height))
