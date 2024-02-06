#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """
        function that writes a string text to a file
        args:
            - filename - file to write to
            - text - string to write
        encodes with utf-8
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(text)
    return len(text)
