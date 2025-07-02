#!/usr/bin/python3
"""
Module 1-my_list
Defines a MyList class that inherits from list and adds a print_sorted method.
"""


class MyList(list):
    """
    MyList inherits from the built-in list.
    
    Public instance method:
        print_sorted(self): Prints the list sorted in ascending order.
    """

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
