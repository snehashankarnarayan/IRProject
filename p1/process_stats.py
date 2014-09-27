#!/usr/bin/python

from collections import Counter
from sets import Set
from statMaster import statMaster

def addUpStats(statList):
    cStats = statMaster()
    for stats in statList:
        cStats.wordCount += stats.wordCount
        cStats.bookUniqueLength += stats.bookUniqueLength
        cStats.pageCount += stats.pageCount
        cStats.bookCount += stats.bookCount
        
    return cStats

def processBulkStats(workerName, statListInQueue, statListOutQueue):
    while True:
        print workerName
        statList = statListInQueue.get()
        cumulativeStats = addUpStats(statList)
        statListOutQueue.put(cumulativeStats)

def processFinalStats(statList):
    return addUpStats(statList) 

def printStats(stats):
    print "Token count: " + str(stats.wordCount)
    print "Unique Token count: " + str(stats.bookUniqueLength)
    print "Page count: " + str(stats.pageCount)
    print "Book count: " + str(stats.bookCount)
