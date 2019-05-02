#!/usr/bin/env python
import re
import math
import sys

class Chromosome:
    """
    chromosome class
    """
    def __init__(self):
        self.sum_length = 0
        self.count = 0

    def avg_size(self):
        return self.sum_length / self.count

    def gene_count(self):
        return self.count

    def add_gene(self, len_gene):
        self.count += 1
        self.sum_length += len_gene

    def __repr__(self):
        return str(self.sum_length, self.count)

if __name__ == "__main__":
    gtfdict = dict()
    tempchrom = re.compile(r"(211|Unmapped)")
    lines = sys.stdin.readlines()
    for line in lines:
        elems = line.rstrip().split('\t')
        if elems[2] == "gene":
            if not tempchrom.match(elems[0]):
                chromo = elems[0]
                length = int(elems[4]) - int(elems[3]) + 1
                if not chromo in gtfdict:
                    gtfdict[chromo] = Chromosome()

                gtfdict[chromo].add_gene(length)

    print("Chromosome,Gene Count,Avg Size")
    for k, v in sorted(gtfdict.items()):
        print(k, v.gene_count(), math.floor(v.avg_size()), sep="\t")

