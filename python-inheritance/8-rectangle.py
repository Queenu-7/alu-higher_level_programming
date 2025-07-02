#!/usr/bin/python3
"""Module defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry as a base."""

    def __init__(self, width, height):
        """Initialize a rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle (must be positive integer).
            height (int): The height of the rectangle (must be positive integer).
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
