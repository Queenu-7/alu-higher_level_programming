#!/usr/bin/python3
"""
Module: 5-save_to_json_file
Writes a Python object to a text file using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file in JSON format.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
