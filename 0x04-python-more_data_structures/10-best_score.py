#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    largest_key = None
    largest_value = 0

    for key, value in a_dictionary.items():
        if value > largest_value:
            largest_key = key
            largest_value = value
    return largest_key
