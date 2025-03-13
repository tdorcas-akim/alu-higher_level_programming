#!/usr/bin/python3
"""Module to append a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to atext file(UTF-8) and returns the number of charcte
    rs."""
    with open(filename, 'a', encoding='utf-8')as file:
        return file.write(text)
