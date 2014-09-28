#!/usr/bin/python

from collections import Counter
from sets import Set
from statMaster import statMaster

def addUpStats(statList):
    cStats = statMaster()
    for stats in statList:
        #Counts
        cStats.wordCount += stats.wordCount
        cStats.bookUniqueLength += stats.bookUniqueLength
        cStats.pageCount += stats.pageCount
        cStats.bookCount += stats.bookCount

        #Global Hashes
        cStats.globalWordHash.update(stats.globalWordHash)
        cStats.bookWordHash.update(stats.bookWordHash)
        cStats.pageWordHash.update(stats.pageWordHash)

        #Special word Hashes
        cStats.strongHash.update(stats.strongHash)
        cStats.strongAdjacentHash.update(stats.strongAdjacentHash)
        cStats.strongWindowHash.update(stats.strongWindowHash)
    
        
    return cStats

def processBulkStats(workerName, statListInQueue, statListOutQueue):
    while True:
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
   
    print stats.globalWordHash.most_common(50)
    print "strong"
    print stats.strongHash.most_common(50)
    print "strong window"
    print stats.strongWindowHash.most_common(50)

    print "strong adjacency"
    print stats.strongAdjacentHash.most_common(50)
    

