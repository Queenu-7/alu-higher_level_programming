#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()  # Should print a 3x3 square of #

print("--")

my_square.size = 10
my_square.my_print()  # Should print a 10x10 square of #

print("--")

my_square.size = 0
my_square.my_print()  # Should print an empty line

print("--")
