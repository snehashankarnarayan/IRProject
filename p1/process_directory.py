#!/usr/bin/python

import xml.etree.cElementTree as ET
import multiprocessing as mp
from os import listdir
import re
import sys
import string
from collections import Counter
from sets import Set
from process_book import processFile
from statMaster import statMaster
from process_stats import processBulkStats, processFinalStats, printStats, outputToFile
import time
from pprint import pprint

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

def touch(statList):
    for stat in statList:
        #i = stat.wordCount
        print "here" + str(stat.wordCount)

def processDirectory(datasize, dirName):
    fileQueue, fileCount = getFileList(dirName)
    fileOutQueue = mp.Queue()
    statListInQueue = mp.Queue()
    statListOutQueue = mp.Queue()
    statListCount = 0
    statFinalList = []
    
    #Some counts
    if(fileCount < 20):
        fileWorkerThreadCount = fileCount
    else:
        fileWorkerThreadCount = 20

    if(fileCount/20 < 10):
        statWorkerThreadCount = fileCount/20 + 1
    else:
        statWorkerThreadCount = 10

    #keep track of processes
    fileworkerList = []
    statworkerList = []

    #statList
    statList = []
    for i in range(0, fileWorkerThreadCount):
        fileworker = mp.Process(target = processFile, args = ("fileworker" + str(i), fileQueue, fileOutQueue, ))
        fileworker.start()
        fileworkerList.append(fileworker)

    for i in range(0, statWorkerThreadCount):
        statworker = mp.Process(target = processBulkStats, args = ("statListWorker" + str(i), statListInQueue, statListOutQueue, ))
        statworker.start()
        statworkerList.append(statworker)

    for i in range(0, fileCount):
        queueElement = fileOutQueue.get()
        print queueElement.wordCount
        print queueElement.globalWordHash.most_common(10)
        print queueElement.bookCount 
        #print queueElement._dict_
        print "inside print"
        pprint(queueElement.__dict__)
        print len(queueElement.globalWordHash)
        statList.append(queueElement)
        if(len(statList) == 20 or len(statList) == fileCount):
            statListInQueue.put(statList)
            touch(statList)
            statListCount += 1
            del statList[:]
        
    #Do a final sweep and add all the stats to be processed to the list    
    for i in range(0, statListCount):
        statFinalList.append(statListOutQueue.get())

    cleanUpProcesses(fileworkerList, statworkerList)
    
    finalstats = processFinalStats(statFinalList)
    printStats(finalstats)

    outputToFile(datasize, finalstats)

def cleanUpProcesses(fileworkerList, statworkerList):
    #Terminate all remaining processes
    for i in range(0, len(fileworkerList)):
        fileworkerList[i].terminate()

    for i in range(0, len(statworkerList)):
        statworkerList[i].terminate()
