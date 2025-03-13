#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, then saves them to a file.
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    items_list = load_from_json_file(filename)
except FileNotFoundError:
    items_list = []

# Add arguments (excluding the script name) to the list
items_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items_list, filename)
