#!/usr/bin/python

from collections import Counter
from sets import Set
from statMaster import statMaster
from heapLaw import heapLaw

class point:
    def __init__(self):
        self.uniqueTokenCount = 0
        self.wordCount = 0

def outputHeapLawData(heapLawList, datasize):
    fp = open("output/snehas_heapLaw_" + datasize + ".txt","w")
    lines = []
    for item in heapLawList:
        line = "(" + str(item.uniqueTokenCount) + "," + str(item.wordCount) + ")\n"
        lines.append(line)

    fp.writelines(lines)
    fp.close()

def processHeapLaw(workerName, inQueue, fileCount, datasize):
    heapLawList = []
    currentTokenSet = Set()
    for i in range(0, fileCount):
        heapL = inQueue.get()
        currentTokenSet.update(heapL.bookWordSet)
        
        pt = point()
        pt.uniqueTokenCount = len(currentTokenSet)
        
        currentLen = len(heapLawList) - 1
        if(currentLen >= 0):
            pt.wordCount = heapLawList[currentLen].wordCount + heapL.wordCount
        else:
            pt.wordCount = heapL.wordCount
        
        heapLawList.append(pt)

    outputHeapLawData(heapLawList, datasize)
