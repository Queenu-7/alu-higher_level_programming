#!/usr/bin/python3
"""
Module: 3-to_json_string
Returns the JSON representation of a Python object (string).
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object.
    """
    return json.dumps(my_obj)
