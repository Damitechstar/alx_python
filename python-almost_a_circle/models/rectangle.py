#!/usr/bin/python3
""" Module for the Rectangle class """
from models.base import Base

class Rectangle(Base):
    """ A class representing a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle's position.
            y (int): Y-coordinate of the rectangle's position.
            id (int): Unique identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Display the rectangle with '#' characters """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Return a string representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update attributes with provided arguments """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for index, arg in enumerate(args):
                if index < len(attrs):
                    setattr(self, attrs[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
