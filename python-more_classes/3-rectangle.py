#!/usr/bin/python3
"""
3-rectangle.py

Defines a Rectangle class with width and height validation,
area and perimeter computation, and custom string representation.
"""


class Rectangle:
    """
    Represents a rectangle with width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width with validation.

        Args:
            value (int): Width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height with validation.

        Args:
            value (int): Height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        Returns 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return the string representation of the rectangle using `#`.

        Returns an empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])
