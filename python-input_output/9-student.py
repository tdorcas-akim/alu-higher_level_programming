#!/usr/bin/python3
"""
This module defines a Student class with attributes and a method to get its di
ctionary representation.
"""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with the given name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the student."""
        return self.__dict__
