#!/usr/bin/python3
"""creates an Object from JSON file"""
import json


def load_from_json_file(filename):
    """returns an object from json file"""
    with open(filename, 'r', encoding='UTF-8') as f:
        x = json.load(f)
    return x
