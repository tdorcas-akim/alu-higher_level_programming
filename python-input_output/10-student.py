#!/usr/bin/python3
"""
This module defines a Student class with attributes and a method to retrieve a
dictionary representationof the student with optional attribute filtering.
"""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the student, filtering by at
        trs if provided."""
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in a
                ttrs}
