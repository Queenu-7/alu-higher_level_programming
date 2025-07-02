#!/usr/bin/python3
"""
Module: 9-rectangle
Defines a Rectangle class with width and height attributes,
capable of calculating area and perimeter, printing the rectangle,
comparing sizes, and creating square instances.
"""


class Rectangle:
    """
    Represents a rectangle shape.

    Attributes:
        number_of_instances (int): The number of Rectangle instances created.
        print_symbol (any): Symbol used for string representation.

    Methods:
        __init__(self, width=0, height=0): Initializes width and height.
        width(self): Getter for width.
        width(self, value): Setter for width with validation.
        height(self): Getter for height.
        height(self, value): Setter for height with validation.
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
        __str__(self): Returns the string representation using print_symbol.
        __repr__(self): Returns a string to recreate the instance.
        __del__(self): Prints a message when an instance is deleted.
        bigger_or_equal(rect_1, rect_2): Static method to compare two rectangles by area.
        square(cls, size=0): Class method to create a square rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter (2*(width + height)), or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return the string representation of the rectangle using print_symbol.

        Returns:
            str: String of the rectangle formed by print_symbol.
                 Empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        line = str(self.print_symbol) * self.width
        rect = (line + "\n") * (self.height - 1) + line
        return rect

    def __repr__(self):
        """
        Return a string representation to recreate a new instance using eval().

        Returns:
            str: String in the format Rectangle(width, height).
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Called when an instance is deleted.

        Prints a message and decrements the number_of_instances counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): First rectangle instance.
            rect_2 (Rectangle): Second rectangle instance.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the larger area,
                       or rect_1 if both are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of the square's sides (default 0).

        Returns:
            Rectangle: New Rectangle instance with width and height equal to size.
        """
        return cls(size, size)

