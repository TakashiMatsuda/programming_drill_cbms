#!/usr/bin/env python

import re

csvpattern = re.compile(r"((\"[[\x00-\x7F]+?\"|[^,]+?),)+?(\"[[\x00-\x7F]+\"|[^,]+?)$")
columnpattern = re.compile(r"(\"[[\x00-\x7F]+?\"|[^,]+?),")
lastcolumn = re.compile(r"(\"[[\x00-\x7F]+?\"|[^,]+?)$")

quotepattern = re.compile(r"\"[[\x00-\x7F]+?\"")
while True:
    try:
        line = input()
    except Exception:
        break
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
            continue
        else:
            break
    print("\t".join(elems))

