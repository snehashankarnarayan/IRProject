#!/usr/bin/python

import sys
from time import time
from process_queries import *

if __name__ == "__main__":
    t1 = time()
    process_queries(sys.argv[1])
    t2 = time()
    minutes = (t2 - t1)/60.0
    fp = open("output/snehas_time.txt", "w")
    line = "Time taken in minutes: " + str(minutes)
    fp.write(line)
    fp.close()
    print 'Time taken in seconds: %f' %(t2-t1)
    print 'Time taken in minutes: ' + str(minutes)
