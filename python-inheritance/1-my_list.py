#!/usr/bin/python3
"""
This module defines the MyList class which inherits from the built-in list.
It provides an additional method to print the list in sorted order without
modifying the original list.
"""


class MyList(list):
    """
    MyList class that extends the built-in list class.
    Adds a method to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Does not modify the original list.
        """
        print(sorted(self))
