#!/usr/bin/python3
"""Defines a Square class with size validation and area calculation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with size, validating its type and value."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
