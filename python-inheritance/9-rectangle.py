#!/usr/bin/python3
"""
9-rectangle.py

This module defines a Rectangle class that inherits from BaseGeometry.
It includes validation for width and height using integer_validator,
calculates area, and provides a custom string representation.
"""


class BaseGeometry:
    """
    BaseGeometry class with a method for validating integers.
    """

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Args:
            name (str): Name of the parameter (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Validates dimensions and calculates area.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: String in the format [Rectangle] width/height
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
