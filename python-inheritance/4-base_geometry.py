#!/usr/bin/python3
class BaseGeometry:
    """
    Empty class representing the base geometry.
    """
    def area(self):
        """
        Calculate the area. This method raises an Exception indicating that it's not implemented.

        :raises: Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")