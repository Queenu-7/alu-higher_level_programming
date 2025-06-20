#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replace an element at a specific index in a copy of the list."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list
    new_list = my_list[:]  # Make a copy
    new_list[idx] = element
    return new_list
