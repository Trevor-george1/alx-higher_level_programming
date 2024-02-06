#!/usr/bin/python3
"""script that adds all arguments to apython list
    and save them to a file
"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    json_list = load_from_json_file(filename)
except (ValueError, FileNotFoundError):
    json_list = []
for arg in sys.argv[1:]:
    json_list.append(arg)
save_to_json_file(json_list, filename)
