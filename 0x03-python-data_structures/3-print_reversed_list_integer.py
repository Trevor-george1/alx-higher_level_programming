#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    new = my_list[::-1]
    for i in new:
        print("{:d}".format(i))
