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
from process_stats import processBulkStats
from process_stats import processFinalStats
import time

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

def output(statList):
    for stat in statList:
        print "here" + str(stat.bookLength)

def processDirectory(dirName):
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
        #print queueElement.bookLength
        statList.append(queueElement)
        if(len(statList) == 20 or len(statList) == fileCount):
            statListInQueue.put(statList)
            output(statList)
            statListCount += 1
            del statList[:]
        
    #Do a final sweep and add all the stats to be processed to the list    
    for i in range(0, statListCount):
        statFinalList.append(statListOutQueue.get())

    cleanUpProcesses(fileworkerList, statworkerList)
    
    finalstats = processFinalStats(statFinalList)
    print "word count: " + str(finalstats.bookLength)


def cleanUpProcesses(fileworkerList, statworkerList):
    #Terminate all remaining processes
    for i in range(0, len(fileworkerList)):
        fileworkerList[i].terminate()

    for i in range(0, len(statworkerList)):
        statworkerList[i].terminate()
