#!/usr/bin/python3
"""
8-rectangle.py

This module defines a Rectangle class that inherits from BaseGeometry.
It validates the width and height using the integer_validator method.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using validated width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
