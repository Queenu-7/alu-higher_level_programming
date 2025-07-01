#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))              # Check class type
print(my_square.__dict__)          # Show instance's internal attributes

try:
    print(my_square.size)          # This should raise an AttributeError
except Exception as e:
    print(e)

try:
    print(my_square.__size)        # This should also raise an AttributeError
except Exception as e:
    print(e)
