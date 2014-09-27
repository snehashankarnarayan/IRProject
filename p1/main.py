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
        processDirectory(tinyDirName)
    elif sys.argv[1] == "small":
        processDirectory(smallDirName)
    elif sys.argv[1] == "medium":
        processDirectory(mediumDirName)
    elif sys.argv[1] == "big":
        processDirectory(bigDirName)
    t2 = time()
    minutes = (t2 - t1)/60.0
    print 'Time taken in seconds: %f' %(t2-t1)
    print 'Time taken in minutes: ' + str(minutes)
