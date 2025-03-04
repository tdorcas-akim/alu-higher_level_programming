#!/usr/bin/python3
"""
This module defines a Rectangle class for calculating area, perimeter, 
and handling instance counting with appropriate validation.
"""


class Rectangle:
    """
    A Rectangle class with width and height attributes, and methods for area, perimeter, 
    string representation, and instance counting.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height values."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width, ensuring it is an integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height, ensuring it is an integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle (width * height)."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle (2 * (width + height))."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns string representation of the rectangle using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += "#" * self.width + "\n"
        return rect_str.strip()

    def __repr__(self):
        """Returns a string to recreate the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message and decrements the instance count when deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
