#!/usr/bin/python3
"""
This module contains a function 'lookup' that returns
a list of available attributes and methods of an object.
"""


def lookup(obj):
    """Return a list of available attributes and methods of obj."""
    return dir(obj)
