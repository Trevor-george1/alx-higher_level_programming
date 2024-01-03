#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new = number
if new < 0:
    new = new * -1
last = new % 10
if last < 6 and last != 0:
    print(f"Last digit of {number:d} is {last:d} and is less than 6 and not 0")
elif last > 5:
    print(f"Last digit of {number:d} is {last:d} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number:d} is {last:d} and is 0")
