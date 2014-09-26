#!/usr/bin/python

import multiprocessing
import xml.etree.cElementTree as ET
from os import listdir
import re
import sys
from time import time
from Queue import Queue

#Constants
tinyDirName = "/phoenix/ir_code/data/books-tiny/"
mediumDirName = "/phoenix/ir_code/data/books-medium/"
smallDirName = "/phoenix/ir_code/data/books-small/"
bigDirName = "/phoenix/ir_code/data/books-big/"

#Globals
global wordCount;

wordlist = []
wordQueue = Queue()

def countString(text, count):
    global wordCount
    words = re.split(" ", text)
    wordcount = count + len(words)
    return wordcount

def getFileList(rootDirName):
    tinyDir =  listdir(rootDirName);
    fileQueue = multiprocessing.Queue()
    fileCount = 0
    for dirName in tinyDir:
        xmlFiles = listdir(rootDirName + dirName)
        for xmlFile in xmlFiles:
            fileQueue.put(rootDirName + dirName + "/" + xmlFile)
            fileCount += 1
    return fileQueue, fileCount

def processFile(processName, fileQueue, outqueue):
    global wordlist
    while(fileQueue.empty() == False):
        count = 0
        fileName = fileQueue.get()
        for event, elem in ET.iterparse(fileName):
            if event == 'end':
                if(elem.text != None):
                    count = countString(elem.text, count)
            elem.clear()
        outqueue.put(count)

def count_words(dirName):
    global wordCount
    wordCount = 0
    
    fileQueue, filecount = getFileList(dirName)
    outqueue = multiprocessing.Queue()
    for i in range(0,5):
        worker = multiprocessing.Process(target = processFile, args = ("worker"+ str(i), fileQueue, outqueue, ))
        worker.start();
    
   
   
    for i in range(0, filecount):
        wordCount += outqueue.get()
    
    print wordCount

if __name__ == "__main__":

    t1 = time()
    if sys.argv[1] == "tiny":
        count_words(tinyDirName)
    elif sys.argv[1] == "small":
        count_words(smallDirName)
    elif sys.argv[1] == "medium":
        count_words(mediumDirName)
    elif sys.argv[1] == "big":
        count_words(bigDirName)
    t2 = time()
    minutes = (t2-t1) / 60.0
    print 'Time taken in seconds: %f' %(t2-t1)
    print 'Time taken in minutes: ' + str(minutes)
    
