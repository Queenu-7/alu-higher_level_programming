#!/usr/bin/python3
"""
11-square.py

This module defines a Square class that inherits from Rectangle.
It validates size during instantiation, computes area, and provides
a custom string representation in the format [Square] width/height.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    A square is a rectangle with equal width and height.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size after validating it.

        Args:
            size (int): The size of the square sides.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: String in the format [Square] size/size
        """
        return f"[Square] {self.__size}/{self.__size}"
