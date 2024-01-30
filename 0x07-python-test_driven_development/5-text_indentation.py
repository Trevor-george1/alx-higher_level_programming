#!/usr/bin/python3
"""
    prints a text with 2 new lines after
    each of these characters ".?:"
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delimeters = ['.', '?', ':']
    for char in text:
        print(char, end='')
        if char in delimeters:
            print("\n" * 2, end='')
