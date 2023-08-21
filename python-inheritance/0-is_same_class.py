#!/usr/bin/python3
"""
Contains a function to check if an object is exactly an instance of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the given class.
    Args:
        obj: The object to be checked.
        a_class: The class to compare against.
    Return: True if the object is an instance of the specified class; otherwise False.
    """
    return type(obj) is a_class