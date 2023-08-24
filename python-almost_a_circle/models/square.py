#!/usr/bin/python3
""" Module for the Square class """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ A class representing a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square instance.

        Args:
            size (int): Size of the square's sides.
            x (int): X-coordinate of the square's position.
            y (int): Y-coordinate of the square's position.
            id (int): Unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return a string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

