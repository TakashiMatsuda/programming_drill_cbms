#!/bin/python
import sys
try:
    fn = input()
    keyword = input()
    wfn = input()
except OSError:
    print("ERROR")
    sys.exit(1)
cnt = 0
with open(fn) as f:
    with open(wfn, "w+") as wf:
        for idx, l in enumerate(f):
            pos = l.find(keyword)
            if pos > -1:
                cnt += 1
                wf.write("line {0}, hit #{1}: ".format(idx+1, cnt) + l)

