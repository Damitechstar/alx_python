#!/usr/bin/python3
"""This module defines the Square class, which provides methods to calculate the area of the square."""

class Square:
    """Represents a square shape with a given size. The size must be a non-negative integer."""

    def __init__(self, size=0):
        """
            Constructs a square object with the specified size.

            Args:
                size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            Calculates and returns the area of the square.
        """
        return self.__size ** 2