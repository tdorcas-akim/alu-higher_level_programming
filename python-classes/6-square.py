#!/usr/bin/python3
"""
This module defines a class Square with private size and position attributes.
It includes methods for area calculation and printing the square with '#' and
position.
"""


class Square:
    """This class defines a square with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with the given size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                        of two positive integers.
            ValueError: If size is less than 0 or if position contains
                        non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with validation.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute with validation.

        Args:
            value (tuple): A tuple of two positive integers representing
                            the position.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If any value in the position tuple is not positive.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' character.

        If size is 0, prints an empty line. The position is taken into
        account to print spaces before the square.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
