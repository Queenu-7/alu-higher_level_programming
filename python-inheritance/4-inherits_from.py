#!/usr/bin/python3
"""Defines inherits_from function."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
