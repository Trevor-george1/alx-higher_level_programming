#!/usr/bin/python3
"""appends a string"""


def append_write(filename="", text=""):
    """function that appends a text at end of file
        args:
                - filename - file to append to
                - text - string to append
        encode in utf-8
    """
    with open(filename, 'a', encoding='UTF-8') as f:
        append_bytes = f.write(text)
    return append_bytes
