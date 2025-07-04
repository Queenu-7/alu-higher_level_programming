#!/usr/bin/python3
"""
1-my_list Module

This module defines the MyList class, which inherits from list
and provides a method to print a sorted version of the list.
"""


class MyList(list):
    """
    MyList class

    Inherits from the built-in list class.
    Provides a public instance method to print the list sorted in ascending order.
    Assumes all elements of the list will be of type int.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.

        Assumes all elements in the list are integers.
        The original list remains unchanged.
        """
        print(sorted(self))
