#!/usr/bin/python3
"""Defnes a class lockedclass"""


class LockedClass:
    """
        prevent the user from dynamically creating new nstance attributes,
        except if the new instance attribute is called firstname
    """
    
    __slots__ = ["first_name"]
    
    def __init__(self):
        """
            creates new instances of locked class
        """
        self.first_name = "first_name"
