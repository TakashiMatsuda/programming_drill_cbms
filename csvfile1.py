#!/usr/bin/env python

origin1 = int(input())-1
origin2 = int(input())-1
while True:
    try:
        line = input()
    except EOFError():
        break
    attributes = line.rstrip().split(",")
    attributes[origin2], attributes[origin1] = attributes[origin1],attributes[origin2]
    buf = ""
    for elem in attributes:
        buf += elem + ","
    print(buf[:-1])

