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

        #Special word Hashes - strong
        cStats.strongHash.update(stats.strongHash)
        cStats.strongAdjacentHash.update(stats.strongAdjacentHash)
        cStats.strongWindowHash.update(stats.strongWindowHash)
    
        #Special word Hashes - powerful
        cStats.powerfulHash.update(stats.powerfulHash)
        cStats.powerfulAdjacentHash.update(stats.powerfulAdjacentHash)
        cStats.powerfulWindowHash.update(stats.powerfulWindowHash)
    
        #Special word Hashes - butter
        cStats.butterHash.update(stats.butterHash)
        cStats.butterAdjacentHash.update(stats.butterAdjacentHash)
        cStats.butterWindowHash.update(stats.butterWindowHash)
    
        #Special word Hashes - salt
        cStats.saltHash.update(stats.saltHash)
        cStats.saltAdjacentHash.update(stats.saltAdjacentHash)
        cStats.saltWindowHash.update(stats.saltWindowHash)
    
        #Special word Hashes - james
        cStats.jamesHash.update(stats.jamesHash)
        cStats.jamesAdjacentHash.update(stats.jamesAdjacentHash)
        cStats.jamesWindowHash.update(stats.jamesWindowHash)
    
        #Special word Hashes - washington
        cStats.washingtonHash.update(stats.washingtonHash)
        cStats.washingtonAdjacentHash.update(stats.washingtonAdjacentHash)
        cStats.washingtonWindowHash.update(stats.washingtonWindowHash)
    
        #Special word Hashes - church
        cStats.churchHash.update(stats.churchHash)
        cStats.churchAdjacentHash.update(stats.churchAdjacentHash)
        cStats.churchWindowHash.update(stats.churchWindowHash)
    
  
    
        
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
    
    print "powerful adjacency"
    print stats.powerfulAdjacentHash.most_common(50)
    
    print "james adjacency"
    print stats.jamesAdjacentHash.most_common(50)
    
    print "salt adjacency"
    print stats.saltAdjacentHash.most_common(50)
    
    print "butter adjacency"
    print stats.butterAdjacentHash.most_common(50)
    
    print "washington adjacency"
    print stats.washingtonAdjacentHash.most_common(50)
    
    print "church adjacency"
    print stats.churchAdjacentHash.most_common(50)
    

