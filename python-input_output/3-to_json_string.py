#!/usr/bin/python3
"""Module to return the json representation of an object."""


import json

def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    try:
        return json.dumps(my_obj)
    except TypeError:
        raise TypeError(f"Object of type {type(my_obj).__name__} is not JSON s
        erializable")
