#!/usr/bin/python

import xml.etree.cElementTree as ET
from os import listdir
import re
import sys
from time import time
import string
from collections import Counter
from sets import Set
from statMaster import statMaster
from process_page import processPage
import multiprocessing as mp

def processFile(workerName, fileQueue, outqueue):
    while True:
        try:
            fileName = fileQueue.get(True, 120)
            #print "Processing: " + fileName
            stats = statMaster()
            stats.bookLength = 0
            stats.bookUniqueLength = 0
            stats.bookWordSet.clear()
            stats.bookCount += 1
            for event, elem in ET.iterparse(fileName):
                if (elem.tag == "page" and event == 'start'):
                    stats.pageText = ""
                if(elem.tag == "line" and event == 'end' and elem.text != None):
                    stats.pageText = stats.pageText + " " + elem.text
                if(elem.tag == "page" and event == 'end'):
                    processPage(workerName, stats)
                    stats.pageText = ""
                elem.clear() 
        
            #Update book hash
            for word in stats.bookWordSet:
                if(stats.bookWordHash.has_key(word)):
                    stats.bookWordHash[word] = stats.bookWordHash[word] + 1
                else:
                    stats.bookWordHash[word] = 1

            stats.bookLengthList.append(stats.wordCount)
            stats.bookUniqueLengthList.append(stats.bookUniqueLength)
            print "Done Processing: " + fileName 
            outqueue.put(stats)
        except:
            pass
    
