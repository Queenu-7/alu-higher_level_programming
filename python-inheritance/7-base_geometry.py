#!/usr/bin/python3
"""
7-base_geometry.py

Defines a BaseGeometry class with an area method placeholder and an
integer_validator method to validate integer inputs.
"""


class BaseGeometry:
    """
    BaseGeometry class with methods area and integer_validator.
    """

    def area(self):
        """
        Public instance method that raises an Exception
        indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

