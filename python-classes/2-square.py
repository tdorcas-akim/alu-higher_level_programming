#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
The private size attribute has validation for type and value.
"""


class Square:
    """This class defines a square with a private size attribute."""

    def__init__(self, size=0):
         """
        Initializes the square with the given size.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
