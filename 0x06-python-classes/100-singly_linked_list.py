#!/usr/bin/python3

"""Define a class Node and a Singly Linked List."""


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node.

    Methods:
        __init__(self, data, next_node=None): Initializes a Node object with a given data value and next node reference.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object.

        Args:
            data (int): The data value to be stored in the node.
            next_node (Node): The reference to the next node (default is None).

        Raises:
            TypeError: If data is not an integer.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node.

        Args:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node): The reference to the head node.

    Methods:
        __init__(self): Initializes a SinglyLinkedList object with an empty list.
        __str__(self): Returns a string representation of the linked list.
        sorted_insert(self, value): Inserts a node with a given value in a sorted manner into the linked list.
    """

    def __init__(self):
        """
        Initializes a SinglyLinkedList object with an empty list.
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Inserts a node with a given value in a sorted manner into the linked list.

        Args:
            value (int): The value to be inserted.

        Notes:
            - If the list is empty, the new node becomes the head.
            - If the value is less than the head's data, the new node becomes the new head.
            - If the value is greater than the head's data, the new node is inserted at the appropriate position.

        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and value > current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
