#!/bin/python

import re
def motif_count(seq, motif):
    start = 0
    count = 0
    while True:
        pos = seq.find(motif, start)
        if pos > -1:
            count += 1
            start = pos + 1
        else:
            return count

motif = input()
d = {}
name = None
seq = None
while True:
    try:
        l = input()
    except EOFError:
        break

    if len(l) > 0 and l[0] == '>':
        if name != None:
            # record the count
            d[name] = motif_count(seq, motif)
        # clear cache
        name = l.rstrip().split()[0][1:]
        seq = ""
        continue
    else:
        seq += l.rstrip()
d[name] = motif_count(seq, motif)
for (k, v) in d.items():
    print(k+":", v)

