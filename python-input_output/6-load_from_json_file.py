#!/usr/bin/python3
"""
Module: 6-load_from_json_file
Creates a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates and returns a Python object from a JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
