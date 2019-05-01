#!/bin/python
import re
# TODO: Realize an unknown reason to be unaccepted
chromosome = re.compile("Chr")
header = re.compile(">")
while True:
    try:
        line = input()
    except EOFError:
        break
    if header.match(line):
        columns = line.split(",")
        geneName = columns[0].split(" ")[1]
        if len(columns) > 1:
            chromosomeName = " ".join(columns[1].strip().split(" ")[:2])
        else:
            chromosomeName = "plasmid"
        if not chromosome.match(chromosomeName):
            chromosomeName = "plasmid"
        print(geneName, chromosomeName, sep=",")

