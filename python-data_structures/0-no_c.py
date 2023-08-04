#!/usr/bin/env python3
from typing import List

def remove_c(my_string: str) -> str:
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string