#!/usr/bin/python3
"""
Contains a function to check if the object is an instance of, 
or if the object is an instance of a class that inherited from, the specified class.
"""
def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of the specified class or its subclasses.
    Args:
        obj: The object to be checked.
        a_class: The class to compare against.
    Return: True if the object is an instance of the specified class or its subclasses; otherwise False.
    """
    return isinstance(obj, a_class)