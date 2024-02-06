#!/usr/bin/python3
"""Reads from a text file"""


def read_file(filename=""):
    """function that reads a file and prints to stdout
        args: filename - name of file to read
        - encodes using UTF-8
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        read_line = f.read()
    print(read_line, end='')