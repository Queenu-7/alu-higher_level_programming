#!/usr/bin/python3
"""
7-base_geometry Module

This module defines the BaseGeometry class, which provides basic
geometric functionality and validation methods.
"""


class BaseGeometry:
    """
    BaseGeometry class

    A base class for geometric shapes, providing common functionality
    like area calculation (to be implemented by subclasses) and
    integer validation for dimensions.
    """

    def area(self):
        """
        Calculates the area of the geometry.

        This method is not implemented in the base class and must be
        overridden by subclasses.

        Raises:
            Exception: Always raises an Exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value.

        Args:
            name (str): The name of the value (e.g., "width", "height").
                        Assumed to be a string.
            value (int): The value to be validated.

        Raises:
            TypeError: If `value` is not an integer.
                       Message: "<name> must be an integer".
            ValueError: If `value` is less than or equal to 0.
                        Message: "<name> must be greater than 0".
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

