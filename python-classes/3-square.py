#!/usr/bin/python3
"""
Defines a Square class with a private size attribute.
Validates size type and value, and calculates area.
"""


class Square:
    """This class defines a square with a private size attribute."""

    def __init__(self, size=0):
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

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
