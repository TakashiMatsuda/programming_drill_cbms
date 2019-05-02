#!/usr/bin/env python
import re
import math

class Chromosome:
    """
    chromosome class
    """
    def __init__(self):
        self.len_genes = []

    def avg_size(self):
        return sum(self.len_genes) / len(self.len_genes)

    def gene_count(self):
        return len(self.len_genes)

    def add_gene(self, len_gene):
        self.len_genes.append(len_gene)

    def __repr__(self):
        return str(self.len_genes)


if __name__ == "__main__":
    gtfdict = dict()
    tempchrom = re.compile(r"(211|Unmapped)")
    while True:
        try:
            line = input()
        except EOFError:
            break
        elems = re.split(r'\t+', line.rstrip())
        if elems[2] == "gene":
            if not tempchrom.match(elems[0]):
                chromo = elems[0]
                length = int(elems[4]) - int(elems[3])
                if not chromo in gtfdict:
                    gtfdict[chromo] = Chromosome()

                gtfdict[chromo].add_gene(length)

    for k, v in sorted(gtfdict.items()):
        print(k, v.gene_count(), math.floor(v.avg_size()), sep="\t")

