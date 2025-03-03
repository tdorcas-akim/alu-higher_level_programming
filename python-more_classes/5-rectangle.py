#!/usr/bin/python3
"""Module containing Rectangle class definition"""


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

    @property
    def height(self):
        """Getter method for height attribute

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute

        Args:
            value (int): Height to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            int: The rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle

        Returns:
            int: The rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle

        Returns:
            str: String representation with # characters
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rectangle_str = []
        for i in range(self.__height):
            rectangle_str.append("#" * self.__width)
        
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Return a string representation of the rectangle for recreation

        Returns:
            str: String representation that can be used with eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
