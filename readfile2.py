#!/bin/python

fn = input()
try:
    f = open(fn, 'r')
    for cnt, line in enumerate(f):
        print(str(cnt+1)+":", line, end="")
except OSError:
    print("ERROR")

