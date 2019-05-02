#!/usr/bin/env python

target_column = int(input())-1
key = input()
header = input()
print(header)
while True:
    try:
        line = input()
    except EOFError():
        break
    attributes = line.rstrip().split(",")
    if attributes[target_column] == key:
        print(line)

