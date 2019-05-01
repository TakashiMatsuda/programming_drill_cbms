#!/bin/python

i = int(input())
j = int(input())

for idx in range(i, j + 1):
    if idx % 3 == 0 and idx % 5 == 0:
        print("Fizz Buzz")
    elif idx % 3 == 0:
        print("Fizz")
    elif idx % 5 == 0:
        print("Buzz")
    else:
        print(idx)

