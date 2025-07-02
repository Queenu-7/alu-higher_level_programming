#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """MyList class that extends list with a print_sorted method."""

    def print_sorted(self):
        """Print the list sorted in ascending order without modifying it."""
        print(sorted(self))
