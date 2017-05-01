#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Increase counters
    for word in words:
        # Write the result to STDOUT (standard output)
        # tab-delimited: the trivial word count is 1
        print '%s\t%s' % (word, 1)