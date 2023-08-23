#!/usr/bin/python3
""" Contains module for the Base class """
class Base:
    """ A base class for managing id attributes """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base instance.

        Args:
            id (int): If specified, set the instance id to this value.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
