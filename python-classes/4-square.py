#!/usr/bin/python3
"""
Defines a Square class with a private size attribute.
Includes getter and setter for size and a method to calculate the area.
"""


class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes the square with the given size.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self.__size = size

    @property
    def size(self):
        """Returns the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
