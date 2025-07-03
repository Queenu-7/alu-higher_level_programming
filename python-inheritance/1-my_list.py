#!/usr/bin/python3
"""
1-my_list.py

Defines a class MyList that inherits from list,
with a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order (without modifying the original list).
        """
        print(sorted(self))
