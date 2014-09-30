#!/usr/bin/python

import sys
from time import time
from process_directory import processDirectory
from dataDirNames import *
    
def testMe():
    fileList = getFileList(tinyDirName)
    processFile(fileList[0])
    print "WordCount " + str(stats.wordCount)
    print "PageCount " + str(stats.pageCount)
    print stats.bookLengthList
    print stats.pageLengthList
    print stats.bookUniqueLengthList
    print stats.pageUniqueLengthList

if __name__ == "__main__":
    t1 = time()
    if sys.argv[1] == "test":
        testMe()
    elif sys.argv[1] == "tiny":
        processDirectory(sys.argv[1], tinyDirName)
    elif sys.argv[1] == "small":
        processDirectory(sys.argv[1], smallDirName)
    elif sys.argv[1] == "medium":
        processDirectory(sys.argv[1], mediumDirName)
    elif sys.argv[1] == "big":
        processDirectory(sys.argv[1], bigDirName)
    t2 = time()
    minutes = (t2 - t1)/60.0
    fp = open("output/snehas_time_" + sys.argv[1] + ".txt", "w")
    line = "Time taken in minutes: " + str(minutes)
    fp.write(line)
    fp.close()
    print 'Time taken in seconds: %f' %(t2-t1)
    print 'Time taken in minutes: ' + str(minutes)
