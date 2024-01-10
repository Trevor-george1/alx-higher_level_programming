#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified = []
    for i in my_list:
        if i == search:
            modified.append(replace)
        else:
            modified.append(i)
    return modified
