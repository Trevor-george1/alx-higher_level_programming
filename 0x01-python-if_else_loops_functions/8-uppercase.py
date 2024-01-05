#!/usr/bin/python3
def uppercase(str):
    new = []
    for i in str:
        print(chr(ord(i) - (ord('a') - ord('A')) if 'a' <= i <= 'z' else ord(i)), end='')
    print()
