#!/usr/bin/env python

import re
import sys

"""
",,,",,,,,,,,,a
,,,%

"""
columnpattern = re.compile(r"(\"[[\x00-\x7F]+?\"|[^,]+?),")
lastcolumn = re.compile(r"(\"[[\x00-\x7F]+?\"|[^,]+?)$")
quotepattern = re.compile(r"\"[[\x00-\x7F]+?\"")
lines = sys.stdin.readlines()
for line in lines:
    elems = []
    while True:
        mch = columnpattern.match(line)
        if mch is not None:
            elems.append(line[mch.span()[0]:mch.span()[1]-1])
            line = line[mch.span()[1]:]
            continue
        elif lastcolumn.match(line) is not None:
            lastmch = lastcolumn.match(line)
            elems.append(line[lastmch.span()[0]:lastmch.span()[1]])
            line = line[lastmch.span()[1]:]
            break
        else:
            next_pos = line.find(",")
            if next_pos != -1:
                elems.append("")
                line = line[next_pos+1:]
                continue
            else:
                break

    row = [x[1:-1] if quotepattern.match(x) else x for x in elems]
    print("\t".join(row))

