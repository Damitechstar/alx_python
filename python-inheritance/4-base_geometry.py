#!/usr/bin/python3
"""Defines a class BaseGeometry (based on 3-base_geometry.py). """
class BaseGeometry:
    """
    Empty class representing the base geometry.
    """
    def area(self):
        """
        This method raises an Exception indicating that it's not implemented.

        Raises: Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
    
class Meta(type):
    """
    Class to remove the __init__subclass the base geometry.
    """
    def __init__(cls, name, bases, attrs):
        if name == 'BaseGeometry':
            attrs.pop('init_subclass', None)
        super().__init__(name, bases, attrs)