#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_elements = []
    total = 0
    for item in my_list:
        if item not in unique_elements:
            unique_elements.append(item)
            total += item
    return total
