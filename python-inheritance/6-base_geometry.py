#!/usr/bin/python3
"""Defines a class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
