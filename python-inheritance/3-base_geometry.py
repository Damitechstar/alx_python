#!/usr/bin/python3
"""A custom metaclass for the BaseGeometry class."""
class BaseGeometryMetaClass(type):
    """Class to remove __init__subclass attribute in base geometry class"""

    def __dir__(cls):
        attrs = super().__dir__()  # Get the default list of attributes
        attrs = [attr for attr in attrs if attr != "__init_subclass__"]  # Exclude "__init_subclass__"
        return attrs
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """Creates an empty class"""
    def __dir__(self):
        attrs = super().__dir__()  # Get the default list of attributes
        attrs = [attr for attr in attrs if attr != "__init_subclass__"]  # Exclude "__init_subclass__"
        return attrs