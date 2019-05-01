#!/bin/python

personindex = dict()
while True:
    p1 = input()
    p2 = input()
    if p1 == "END" and p2 == "END":
        break
    for p in [p1, p2]:
        if p in personindex:
            personindex[p] += 1
        else:
            personindex[p] = 1

# select a person who has the most
bestnum = 0
bestp = None
for (k, v) in personindex.items():
    if v > bestnum:
        bestp = k
        bestnum = v

print(bestp, bestnum)


