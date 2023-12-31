#!/usr/bin/python3
"""
    This module defines the Square class, which provides properties to get and set the size of the square.
"""

class Square:
    """Represents a square shape with a given size."""
    def __init__(self, size=0):
        """Constructs a square object with the specified size.
            Args:
                size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Prints a visual representation of the square using the '#' character.
            If the size of the square is 0, it prints an empty line."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)