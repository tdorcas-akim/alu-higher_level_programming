#!/usr//bin/python 3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        if isinstance(value, int):
            new_dict[key] = value * 2
    return new_dict
