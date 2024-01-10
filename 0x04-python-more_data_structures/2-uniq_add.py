#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    for i in my_list:
        unique.add(i)
    sum_unique = sum(unique)
    return sum_unique
