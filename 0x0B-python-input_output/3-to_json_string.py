#!/usr/bin/python3
import json
"""Json representation of a string"""


def to_json_string(my_obj):
    """function that returns a json object from string obj
        args:
            - obj - string object
    """
    json_string = json.dumps(my_obj)
    return json_string
