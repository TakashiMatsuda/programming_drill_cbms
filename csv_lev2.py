#!/usr/bin/env python

import re

csvpattern = re.compile(r"((\"[[\x00-\x7F]+?\"|[^,]+?),)+?(\"[[\x00-\x7F]+\"|[^,]+)$")
target = input()
print(csvpattern.sub(r'\2\t\3', target))

