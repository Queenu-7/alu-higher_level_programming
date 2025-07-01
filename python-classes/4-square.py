#!/usr/bin/python3
"""
This module defines a Square class that includes size validation,
allows access and modification of the size attribute through
property methods, and provides a method to calculate the area of the square.
"""

class Square:
    def __init__(self, size=0):
        self.size = size  # Will use the setter for validation

    @property
    def size(self):
        return self.__size  # return the private attribute

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # set the private attribute

    def area(self):
        return self.__size * self.__size
