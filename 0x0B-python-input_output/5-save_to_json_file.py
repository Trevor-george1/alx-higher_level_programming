#!/usr/bin/python3
"""writes an Object to a text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes json string to a file
        args:
            * my_obj: python data structure
            * filename: file to write to
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        json_string = json.dump(my_obj, f)
