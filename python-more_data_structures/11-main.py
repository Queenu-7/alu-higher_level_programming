#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)  # Should print: [4, 8, 12, 16, 24]
print(my_list)   # Should print: [1, 2, 3, 4, 6]
