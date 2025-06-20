#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]

# Test valid replacement
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)
print(new_list)   # Expected: [1, 2, 3, 9, 5]
print(my_list)    # Expected: [1, 2, 3, 4, 5] (unchanged)

# Test negative index
idx = -1
new_list = new_in_list(my_list, idx, new_element)
print(new_list)   # Expected: [1, 2, 3, 4, 5] (copy unchanged)

# Test index out of range
idx = 10
new_list = new_in_list(my_list, idx, new_element)
print(new_list)   # Expected: [1, 2, 3, 4, 5] (copy unchanged)
