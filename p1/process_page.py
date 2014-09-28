#!/usr/bin/python

import xml.etree.cElementTree as ET
from os import listdir
import re
import sys
from time import time
import string
from collections import Counter
from sets import Set

def checkAndUpdate(stats, key, word):

    if(key == "normal"):
        if(stats.pageWordHash.has_key(word)):
            stats.pageWordHash[word] = stats.pageWordHash[word] + 1
        else:
            stats.pageWordHash[word] = 1
    
    elif(key == "strong"):
        if(stats.strongHash.has_key(word)):
            stats.strongHash[word] = stats.strongHash[word] + 1
        else:
            stats.strongHash[word] = 1

def initializeExistenceMap(exist):
    exist["strong"] = False
    exist["powerful"] = False
    exist["salt"] = False
    exist["butter"] = False
    exist["james"] = False
    exist["church"] = False
    exist["washington"] = False
    return exist

def checkExistence(existenceMap, key, word):
    if(existenceMap[key] == False):
        existenceMap[key] = re.match(key, word, re.IGNORECASE) 
    return existenceMap

def processPage(workername, stats):
    #print workername + ":" + str(stats.bookLength)
    stats.pageCount = stats.pageCount + 1
   
    #Text processing in page
    words = re.split(" ", stats.pageText)
    for i in range(0, len(words) - 1):
        words[i] = words[i].translate(None, string.punctuation).strip().lower()

        if(stats.globalWordHash.has_key(words[i])):
            stats.globalWordHash[words[i]] = stats.globalWordHash[words[i]] + 1
        else:
            stats.globalWordHash[words[i]] = 1
    
    stats.pageLengthList.append(len(words))
    stats.wordCount = stats.wordCount + len(words)

    #Unique words in Page specific processing
    wordSet = set(words)

    existenceMap= {}
    existenceMap = initializeExistenceMap(existenceMap)

    for word in wordSet:
        word = word.translate(None, string.punctuation)
       
        existenceMap = checkExistence(existenceMap, "strong", word)
        existenceMap = checkExistence(existenceMap, "powerful", word)
        existenceMap = checkExistence(existenceMap, "salt", word)
        existenceMap = checkExistence(existenceMap, "butter", word)
        existenceMap = checkExistence(existenceMap, "james", word)
        existenceMap = checkExistence(existenceMap, "church", word)
        existenceMap = checkExistence(existenceMap, "powerful", word)
        
        #Check normal word hash
        checkAndUpdate(stats, "normal", word)
    
    for word in wordSet:
        checkAndUpdate(stats, "strong", word)
    
    stats.bookWordSet.update(wordSet)
    stats.pageUniqueLengthList.append(len(wordSet))
    stats.bookUniqueLength = stats.bookUniqueLength + len(wordSet)

    stats.pageText = ""    


