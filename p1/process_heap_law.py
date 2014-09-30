#!/usr/bin/python

from collections import Counter
from sets import Set
from statMaster import statMaster
from heapLaw import heapLaw
import traceback

class point:
    def __init__(self):
        self.uniqueTokenCount = 0
        self.wordCount = 0

def outputHeapLawData(heapLawList, datasize):
    print "Outputting heap"
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
        try:
            print "processing heap: " + str(i) 
            heapL = inQueue.get(True, 240)
            currentTokenSet.update(heapL.bookWordSet)
        
            pt = point()
            pt.uniqueTokenCount = len(currentTokenSet)
        
            currentLen = len(heapLawList) - 1
            if(currentLen >= 0):
                pt.wordCount = heapLawList[currentLen].wordCount + heapL.wordCount
            else:
                pt.wordCount = heapL.wordCount
        
            heapLawList.append(pt)
        except:
            print traceback.format_exc()
            break

    outputHeapLawData(heapLawList, datasize)
