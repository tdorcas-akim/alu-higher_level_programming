#!/usr/bin/python3
""" It prints the first and last name. """


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"
    
    Args:
        first_name (str): The first name.
        last_name (str): The last name. Default is an empty string.
        
    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
