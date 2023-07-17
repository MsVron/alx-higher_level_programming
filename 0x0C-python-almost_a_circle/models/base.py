#!/usr/bin/python3

"""Base class for managing id attribute in all future classes."""


class Base:

    """
    Initialize a Base instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id (int, optional): The id of the instance.
                If provided, the id attribute will be set to this value.
                If not provided, the id attribute will be incremented using
                the __nb_objects attribute.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
