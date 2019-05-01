#!/bin/python

with open("test.txt", 'r') as f:
    print(len([x for x in f]))

