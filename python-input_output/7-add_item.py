#!/usr/bin/python3
"""
Script: 7-add_item
Adds command line arguments to a Python list and saves them in a JSON file.
"""

import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing data if file exists; otherwise, start with empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add new command-line arguments
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
