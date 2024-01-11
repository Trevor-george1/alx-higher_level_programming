#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    new.update(a_dictionary)
    for key in new:
        new[key] *= 2
    return new
