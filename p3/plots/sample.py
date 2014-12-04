#!/usr/bin/python

import sys

fp = open(sys.argv[1], "r")
outfile = open(sys.argv[1] + "-sample", "w")

count = 0
for line in fp:
    if(count == 9):
        outfile.write(line)
        count = 0
    count += 1

fp.close()
outfile.close()



