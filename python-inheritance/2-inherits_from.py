#!/usr/bin/python3
"""
Contains a function to check  if the object is an instance of a class that inherited 
(directly or indirectly) from the specified class.
"""
def inherits_from(obj, a_class):
    """
    Check if the given object is an instance of a class that inherits from the specified class.
    Args:
        obj: The object to be checked.
        a_class: The class to compare against.
    Return: True if the object is an instance of a class that inherits from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
