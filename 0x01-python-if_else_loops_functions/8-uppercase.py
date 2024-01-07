#!/usr/bin/python3
def uppercase(str):
    for i in str:
        t = i
        if ord(t) >= 97 and ord(t) <= 122:
            t = chr(ord(i) - 32)
        print("{}".format(t), end='')
    print()
