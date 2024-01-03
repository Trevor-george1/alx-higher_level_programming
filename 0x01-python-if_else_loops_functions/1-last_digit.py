#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    neg = number % (-10)
else:
    neg = number % 10
if neg < 6 and neg != 0:
    print(f"Last digit of {number:d} is {neg:d} and is less than 6 and not 0")
elif neg > 5:
    print(f"Last digit of {number:d} is {neg:d} and is greater than 5")
elif neg == 0:
    print(f"Last digit of {number:d} is {neg:d} and is 0")
