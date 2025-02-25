#!/usr/bin/python3
"""
Defines a Square class with a private size and area method.
Validates size type and value.
"""

class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes square with size.

        Args:
            size (int): Size of square, default is 0.
        
        Raises:
            TypeError: If size isn't an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
