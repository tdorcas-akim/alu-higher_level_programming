#!/usr/bin/python3
"""
Module that provides a function to write an object to a text file using a JSON
representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to be serialized and saved.
        filename (str): The name of the file where the object will be saved.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
