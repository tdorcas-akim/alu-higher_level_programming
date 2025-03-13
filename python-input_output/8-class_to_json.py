#!/usr/bin/python3
"""
This module defines the function class_to_json that converts an object to a di
ctionary.
"""


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structure for JSON seria
    lization
    """

    return obj.__dict__
