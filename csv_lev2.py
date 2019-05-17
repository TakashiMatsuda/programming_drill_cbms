#!/usr/bin/env python

import re

csvpattern = re.compile(r"((\"[[\x00-\x7F]+?\"|[^,]+?),)+?(\"[[\x00-\x7F]+\"|[^,]+)$")
quotepattern = re.compile(r"\"[[\x00-\x7F]+?\"")
while True:
    try:
        line = input()
    except Exception:
        break
    matches = csvpattern.match(line)
    row = matches.group(2, 3)
    row = [x[1:-1] if quotepattern.match(x) else x for x in row]
    print("\t".join(row))
#
#    id_ = csvpattern.match(line, 3)
#    name = name[1:-1] if quotepattern.match(name) else name
#    id_ = id_[1:-1] if quotepattern.match(id_) else id_
#    print("\t".join([name, id_]))
