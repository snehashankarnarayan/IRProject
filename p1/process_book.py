#!/usr/bin/python

import xml.etree.cElementTree as ET
from os import listdir
import re
import sys
from time import time
import string
from collections import Counter
from sets import Set
from globalvars import stats
from process_page import processPage

w1list = ["strong","powerful","butter","salt"]
w2list = ["strong","powerful","butter","salt"]

def processFile(fileName):

    stats.bookLength = 0
    stats.bookUniqueLength = 0
    stats.bookCount = stats.bookCount + 1
    stats.bookWordSet.clear()
    for event, elem in ET.iterparse(fileName):
        if (elem.tag == "page" and event == 'start'):
            stats.pageText = " "
        if(elem.tag == "line" and event == 'end' and elem.text != None):
            stats.pageText = stats.pageText + " " + elem.text
        if(elem.tag == "page" and event == 'end'):
            processPage()
        elem.clear() 

    #Update book hash
    for word in stats.bookWordSet:
        if(stats.bookWordHash.has_key(word)):
            stats.bookWordHash[word] = stats.bookWordHash[word] + 1
        else:
            stats.bookWordHash[word] = 1

    stats.bookLengthList.append(stats.bookLength)
    stats.bookUniqueLengthList.append(stats.bookUniqueLength)
    