#!/usr/bin/python3
"""Json string to python data structure"""
import json
from io import StringIO


def from_json_string(my_str):
    """returns an object rep by a JSON string
        args: my_str - string to convert
    """
    py_ob = StringIO(my_str)
    return json.load(py_ob)
