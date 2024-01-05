#!/usr/bin/python3
if __name__ == '__main__':
    """result of addition of all arguments"""
    import sys

    args = sys.argv[1:]
    count = sum(map(int, args))
    if count == 0:
        print("0")
    else:
        print(count)
