#!/usr/bin/python3
"""
This module defines a Square class with size and position,
and provides methods to compute area and print the square
visually using the `#` character with spacing.
"""


class Square:
    """
    Represents a square with size and position.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position (x, y) offset for printing.

    Methods:
        size (property): Getter/setter for size.
        position (property): Getter/setter for position.
        area(): Returns area of the square.
        my_print(): Prints the square using # characters.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square.

        Args:
            size (int): Size of the square (default 0).
            position (tuple): Position as (x, y) offset (default (0, 0)).

        Raises:
            TypeError: If size is not an int or position is not a valid tuple.
            ValueError: If size is negative or position has negative values.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' based on size and position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # print vertical offset (new lines)
        for _ in range(self.__position[1]):
            print()

        # print each row with horizontal offset (spaces)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
