#!/usr/bin/python3
"""Module to write a string and return the number of characters."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
