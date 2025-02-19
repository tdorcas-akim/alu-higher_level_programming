#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for key in sorted_keys:
        if key in a_dictionary:
            value = a_dictionary[key]
            print(f"{key}: {value}")
