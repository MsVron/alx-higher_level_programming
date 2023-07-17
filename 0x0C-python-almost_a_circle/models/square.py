#!/usr/bin/python3

"""Class representing a Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        size (int): side length of the square.
        x (int, optional): x coordinate of the square. Defaults to 0.
        y (int, optional): y coordinate of the square. Defaults to 0.
        id (int, optional): id of the square. If not provided, an id is
            automatically assigned using the logic from the Base class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): side length of the square.
            x (int, optional): x coordinate of the square. Defaults to 0.
            y (int, optional): y coordinate of the square. Defaults to 0.
            id (int, optional): id of the square. If not provided, an id is
                automatically assigned using the logic from the Base class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the Square instance.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
