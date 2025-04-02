#!/usr/bin/python3
""" This will print a square with a character #. """


def print_square(size):
    """
    Prints a square with the character '#' of a given size.

    Args:
        size (int): The length of the square's side.

    Raises:
        TypeError: If size is not an int or is a float and less than 0.
        ValueError: If size is less than 0.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
