#!/usr/bin/python3
"""
This module defines the MyList class which inherits from list
and includes a method to print the list in sorted order.
"""


class MyList(list):
    """A subclass of list with a method to print a sorted version."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (does not modify original)."""
        print(sorted(self))
