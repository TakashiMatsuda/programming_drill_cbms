#!/usr/bin/env python
import re
import sys

pattern = re.compile(r"Adding sequences from .....; added [0-9]+? sequences")

lines = sys.stdin.readlines()
for l in lines:
    result = pattern.search(l)
    if result != None:
        print(l.rstrip().split(" ")[5])

