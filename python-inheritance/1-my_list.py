#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from list.
"""


class MyList(list):
    """
    A class MyList that inherits from list.

    Provides a method to print the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Assumes all elements of the list are of type int.
        """
        # Create a sorted copy of the list and print it.
        # The original list remains unchanged.
        print(sorted(self))
