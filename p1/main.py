#!/usr/bin/python

import xml.etree.cElementTree as ET
import multiprocessing as mp
from os import listdir
import re
import sys
from time import time
import string
from collections import Counter
from sets import Set
from process_book import processFile
from dataDirNames import *
from statMaster import statMaster
from process_stats import processBulkStats
from process_stats import processFinalStats

def getFileList(rootDirName):
    tinyDir =  listdir(rootDirName);
    fileQueue = mp.Queue()
    fileCount = 0
    for dirName in tinyDir:
        xmlFiles = listdir(rootDirName + dirName)
        for xmlFile in xmlFiles:
            fileQueue.put(rootDirName + dirName + "/" + xmlFile)
            fileCount += 1
    return fileQueue, fileCount

def processDirectory(dirName):
    fileQueue, fileCount = getFileList(dirName)
    try:
        fileOutQueue = mp.Queue()
        statListInQueue = mp.Queue()
        statListOutQueue = mp.Queue()
        statListCount = 0

        statFinalList = []

        for i in range(0, 20):
            fileworker = mp.Process(target = processFile, args = (fileQueue, fileOutQueue, ))
            fileworker.start()
        
        for i in range(0, 10):
            statworker = mp.Process(target = processBulkStats, args = (statListInQueue, statListOutQueue, ))
            statworker.start()

        for i in range(0, fileCount):
            statList = []
            output = fileOutQueue.get()
            statList.add(fileOutQueue.get())

            if(i % 20 == 0 or i == fileCount - 1):
                statListInQueue.put(statList)
                statList.clear()
                statListCount += 1
        

        for i in range(0, statListCount):
            statFinalList.add(statListOutQueue.get())

        finalstats = processFinalStats(statFinalList)
        print finalstats.wordCount
    
    except (xml.etree.ElementTree.ParseError, RuntimeError, TypeError, NameError):
        pass
    except (RuntimeError, TypeError, NameError):
        pass
    except:
        print "Unexpected Error.. Continue anyway"
        pass

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
    print 'Time taken in seconds: %f' %(t2-t1)
