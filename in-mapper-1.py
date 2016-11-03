#!/usr/bin/env python
# mapper.py
# Sheng Zhou
# A mapper program for a hadoop WordCount program
import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    n = 0
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if n % 2 == 1:
                print '%s\t%s' % (word, 1)
        n += 1
