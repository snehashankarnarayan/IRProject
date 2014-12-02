#!/usr/bin/python

from pprint import pprint
from time import time
import subprocess
import sys

def processFile(fileName, outfile):
    fp = open(outfile, "w")
    lines = []
    command = "/home/sneha/phoenix/galago/galago-3.6-bin/bin/galago batch-search --index='/phoenix/ir_code/galago-index-books' --requested=100 " + fileName
    outl = subprocess.check_output(command, shell=True) 
    out = outl.split('\n')
    for inline in out:
        parts = inline.split(" ")
        if(len(parts) > 1):
            parts[1] = "0"
            line = " ".join(parts)
            line = line + '\n'
            lines.append(line)
    fp.writelines(lines)
    fp.close()

if __name__ == "__main__":

    t1 = time()
    processFile(sys.argv[1], sys.argv[2])
    t2 = time()
    print 'Time taken in seconds: %f' %(t2-t1)
