#!/usr/bin/python3
"""
This module defines a Student class with attributes and a method to retrieve a
dictionary representation.
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
        if attrs is None:
            return self.__dict_
        return {key: value for key, value in self.__dict__.items() if key in attrs}
