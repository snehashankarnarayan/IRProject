#!/usr/bin/python

from collections import Counter
from sets import Set
from statMaster import statMaster

def processBulkStats(workerName, statListInQueue, statListOutQueue):
    while True:
        print workerName
        statList = statListInQueue.get()
        cumulativeStats = statMaster()
        for stats in statList:
            '''cumulativeStats.wordCount += stats.wordCount
            cumulativeStats.pageCount += stats.pageCount
            cumulativeStats.bookCount += stats.bookCount
            #cumulativeStats.wordCount += stats.wordCount
    '''
            cumulativeStats.bookLength += stats.bookLength
        statListOutQueue.put(cumulativeStats)

def processFinalStats(statList):
    finalStats = statMaster()
    for stats in statList:
        finalStats.bookLength += stats.bookLength
    return finalStats 
