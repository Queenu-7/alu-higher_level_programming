#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

# Create a rectangle of width 2 and height 4
my_rectangle = Rectangle(2, 4)

# Print area and perimeter
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# Print string representation (the rectangle shape)
print(str(my_rectangle))

# Print the repr representation
print(repr(my_rectangle))

print("--")

# Change dimensions
my_rectangle.width = 10
my_rectangle.height = 3

# Print rectangle again using __str__
print(my_rectangle)

# Print the repr representation again
print(repr(my_rectangle))
