#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number if isinstance(x, int) else x, 
                    my_list))
