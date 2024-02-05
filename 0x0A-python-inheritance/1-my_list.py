#!/usr/bin/python3
"""
    class that inherits from list
"""


class MyList(list):
    """
        prints the list in sorted form
    """
    def print_sorted(self):
        new = []
        new = sorted(self)
        print(new)
