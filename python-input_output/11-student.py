#!/usr/bin/python3
"""
This module defines a Student class with methods to serialize and deserialize the obj.
"""


class Student:
    """Student class with first name, last name, and age attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student, filtered by attr
        s."""
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in a
                ttrs}

    def reload_from_json(self, json):
        """Update the student's attributes from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
