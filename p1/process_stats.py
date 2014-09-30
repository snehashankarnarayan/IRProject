#!/usr/bin/python

from collections import Counter
from sets import Set
from statMaster import statMaster
import gc

def addUpStats(statList):
    cStats = statMaster()
    counter = 0
    for stats in statList:
        print "Consolidating stats ... " 
        #Counts
        cStats.wordCount += stats.wordCount
    #    cStats.bookUniqueLength += stats.bookUniqueLength
        cStats.pageCount += stats.pageCount
        cStats.bookCount += stats.bookCount
        cStats.bookWordSet.update(stats.bookWordSet)
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
        cStats.jamesPrecedingHash.update(stats.jamesPrecedingHash)
        cStats.jamesAdjacentHash.update(stats.jamesAdjacentHash)
        cStats.jamesWindowHash.update(stats.jamesWindowHash)
    
        #Special word Hashes - washington
        cStats.washingtonHash.update(stats.washingtonHash)
        cStats.washingtonPrecedingHash.update(stats.washingtonPrecedingHash)
        cStats.washingtonAdjacentHash.update(stats.washingtonAdjacentHash)
        cStats.washingtonWindowHash.update(stats.washingtonWindowHash)
    
        #Special word Hashes - church
        cStats.churchHash.update(stats.churchHash)
        cStats.churchPrecedingHash.update(stats.churchPrecedingHash)
        cStats.churchAdjacentHash.update(stats.churchAdjacentHash)
        cStats.churchWindowHash.update(stats.churchWindowHash)
        
        if(counter%100 == 0):
            gc.collect()

    return cStats

def processBulkStats(workerName, statListInQueue, statListOutQueue):
    while True:
        try:
            statList = statListInQueue.get()
            cumulativeStats = addUpStats(statList)
            statListOutQueue.put(cumulativeStats)
        except:
            pass

def processFinalStats(statList):
    return addUpStats(statList) 

def printStats(stats):
    print "Token count: " + str(stats.wordCount)
    print "Unique Token count: " + str(stats.bookUniqueLength)
    print "Page count: " + str(stats.pageCount)
    print "Book count: " + str(stats.bookCount)
    print "washington"
    print stats.washingtonHash.most_common(50)
    print "strong"
    print stats.strongHash.most_common(50)
    print "butter"
    print stats.butterHash.most_common(50)
    print "powerful"
    print stats.powerfulHash.most_common(50)
    print "salt"
    print stats.saltHash.most_common(50)
    print "church"
    print stats.churchHash.most_common(50)
    print "james"
    print stats.jamesHash.most_common(50)
   
def computeExtraStats(datasize, stats):
    fp = open("output/special_stats_" + datasize + ".txt", "w")
    lines = []

    #Analyze strong
    wordlist = stats.strongHash.most_common(10)
    
    for item in wordlist:
        line = "Strong " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)
    
    #Analyze powerful
    wordlist = stats.powerfulHash.most_common(10)
    
    for item in wordlist:
        line = "powerful " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)
    
    #Analyze salt
    wordlist = stats.saltHash.most_common(10)
    
    for item in wordlist:
        line = "salt " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)

    #Analyze butter
    wordlist = stats.butterHash.most_common(10)
    
    for item in wordlist:
        line = "butter " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)

    #Word adjacency - james
    wordlist = stats.jamesAdjacentHash.most_common(5)
    prelist = stats.jamesPrecedingHash.most_common(5)
    
    for item in wordlist:
        line = "James " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)
    
    for item in prelist:
        line = "James precedence " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)
    
    #Word adjacency - washington
    wordlist = stats.washingtonAdjacentHash.most_common(5)
    prelist = stats.washingtonPrecedingHash.most_common(5)
    
    for item in wordlist:
        line = "washington " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)

    for item in prelist:
        line = "washington precedence " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)
    
    #Word adjacency - church
    wordlist = stats.churchAdjacentHash.most_common(5)
    prelist = stats.churchPrecedingHash.most_common(5)
    
    for item in wordlist:
        line = "church " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)
    
    for item in prelist:
        line = "church precedence " + item[0] + " " + str(item[1]) + "\n"
        lines.append(line)
    
    #Final write
    fp.writelines(lines)
    fp.close()

