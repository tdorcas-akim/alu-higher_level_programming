#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """Class that defines a rectangle with width and height attributes"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width attribute

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute

        Args:
            value (int): Width to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

def height(self):
    """ method that returns the value of the height

    Returns:
        height of the rectangle


    """
 

   return self.__height

def height(self, value):
    """ method that defines the height

    Args:
        value: height

    Raises:
        TypeError: if height is not an integer
        ValueError: if height is less than zero


        """
 

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
