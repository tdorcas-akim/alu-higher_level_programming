#!/usr/bin/python3
"""Module to read and print the contents of a file."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
