#!/usr/bin/python3
"""
Module that provides a function to return an object (Python data structure)
represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """
    Returns the object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to an object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
