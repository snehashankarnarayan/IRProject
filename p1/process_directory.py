#!/usr/bin/python

import traceback
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
from process_stats import processBulkStats, processFinalStats, printStats, computeExtraStats
from generate_output import generate_output
import time
import gc
from heapLaw import heapLaw
from process_heap_law import processHeapLaw, outputHeapLawData

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
    fp = open("trash.txt","w")
    for stat in statList:
        #i = stat.wordCount
        fp.write(str(stat.wordCount))
        #print "here" + str(stat.wordCount)

def processDirectory(datasize, dirName):
    fileQueue, fileCount = getFileList(dirName)
    fileOutQueue = mp.Queue()
    statListInQueue = mp.Queue()
    statListOutQueue = mp.Queue()
    heapInQueue = mp.Queue()
    statListCount = 0
    statFinalList = []
    
    #Some counts
    if(fileCount < 8):
        fileWorkerThreadCount = fileCount
    else:
        fileWorkerThreadCount = 8

    if(fileCount/4 < 4):
        statWorkerThreadCount = fileCount/4 + 1
    else:
        statWorkerThreadCount = 4

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

    #Deal with heaplaw
    heapworker = mp.Process(target = processHeapLaw, args = ("heapworker", heapInQueue, fileCount, datasize, ))
    heapworker.start()

    for i in range(0, fileCount):
        try:
            queueElement = fileOutQueue.get(True, 240)
            statList.append(queueElement)
            heapL = heapLaw()
            heapL.bookWordSet = queueElement.bookWordSet
            heapL.wordCount = queueElement.wordCount
            heapInQueue.put(heapL)
            if(len(statList) == 20 or i == fileCount-1):
                statListInQueue.put(statList)
                print "element going into statlistinqueue {} {}".format(i, fileCount)
                touch(statList)
                statListCount += 1
                del statList[:] 
                gc.collect()

        except:
            print traceback.format_exc()
            break
            
    cleanUpProcesses(fileworkerList)
    print "statListcount {}".format(statListCount) 
    #Do a final sweep and add all the stats to be processed to the list    
    for i in range(0, statListCount):
        try:
            statFinalList.append(statListOutQueue.get(True, 240))
            print "received statlists {}".format(i)
            if(i % 100 == 0):
                gc.collect()
        except:
            print traceback.format_exc()
            break

    cleanUpProcesses(statworkerList)
    print "FINAL STATS COMPILATION"
    finalstats = processFinalStats(statFinalList)
    #printStats(finalstats)
    computeExtraStats(datasize, finalstats)
    generate_output(datasize, finalstats)
    heapworker.terminate()

def cleanUpProcesses(fileworkerList):
    
    print "cleaning up processes"
    
    #Terminate all remaining processes
    for i in range(0, len(fileworkerList)):
        fileworkerList[i].terminate()
