#!/usr/bin/python3
"""
Module that provides a function to return the JSON representation of an obj.
"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    
    Args:
        my_obj (any type): The object to be converted to JSON string.
    
    Returns:
        str: The JSON representation of the object as a string.
    
    Raises:
        TypeError: If the object can't be serialized to JSON.
    """
    try:
        return json.dumps(my_obj)
    except TypeError:
        raise TypeError(f"Object of type {type(my_obj).__name__} is not JSON s
        erializable")
