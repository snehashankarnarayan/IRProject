#!/usr/bin/python

import xml.etree.cElementTree as ET
from os import listdir
import re
import sys
from time import time
import string
from collections import Counter
from sets import Set


w1list = ["strong","powerful","butter","salt"]
w2list = ["strong","powerful","butter","salt"]

def processPage(stats):
    stats.pageCount = stats.pageCount + 1
    
    #Text processing in page
    words = re.split(" ", stats.pageText)
    for i in range(0, len(words) - 1):
        words[i] = words[i].translate(None, string.punctuation)

        if(stats.globalWordHash.has_key(words[i])):
            stats.globalWordHash[words[i]] = stats.globalWordHash[words[i]] + 1
        else:
            stats.globalWordHash[words[i]] = 1
    
    stats.pageLengthList.append(len(words))
    stats.bookLength = stats.bookLength + len(words)
    #Page specific processing
    wordSet = set(words)
    for word in wordSet:
        word = word.translate(None, string.punctuation)
        if(stats.pageWordHash.has_key(word)):
            stats.pageWordHash[word] = stats.pageWordHash[word] + 1
        else:
            stats.pageWordHash[word] = 1
    
    stats.bookWordSet.update(wordSet)
    stats.pageUniqueLengthList.append(len(wordSet))
    stats.bookUniqueLength = stats.bookUniqueLength + len(wordSet)




