#!/usr/bin/python3
for c in range(97, 123):
    if c == 113:
        continue
    if c == 101:
        continue
    print("{:c}".format(c), end='')
