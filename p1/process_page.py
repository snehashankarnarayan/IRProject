#!/usr/bin/python

import xml.etree.cElementTree as ET
from os import listdir
import re
import sys
from time import time
import string
from collections import Counter
from sets import Set
from stopwords import *

def checkAndUpdate(stats, key, word):
    if(key == "normal"):
        if(stats.pageWordHash.has_key(word)):
            stats.pageWordHash[word] = stats.pageWordHash[word] + 1
        else:
            stats.pageWordHash[word] = 1
    
    elif(key == "strong" and word not in stopwords):
        if(stats.strongHash.has_key(word)):
            stats.strongHash[word] = stats.strongHash[word] + 1
        else:
            stats.strongHash[word] = 1

def checkAndUpdateAdjacency(stats, word, eMap, key): 
    if(eMap[key] == True):
        if(key == "strong" and word not in stopwords):
            if(stats.strongAdjacentHash.has_key(word)):
                stats.strongAdjacentHash[word] = stats.strongAdjacentHash[word] + 1
            else:
                stats.strongAdjacentHash[word] = 1


def checkAndUpdateWindowHash(stats, word, eMap, key): 
    if(eMap[key] == True):
        if(key == "strong" and word not in stopwords):
            if(stats.strongWindowHash.has_key(word)):
                stats.strongWindowHash[word] = stats.strongWindowHash[word] + 1
            else:
                stats.strongWindowHash[word] = 1
    

def initializeExistenceMap(exist):
    exist["strong"] = False
    exist["powerful"] = False
    exist["salt"] = False
    exist["butter"] = False
    exist["james"] = False
    exist["church"] = False
    exist["washington"] = False
    return exist

def checkExistence(existenceMap, adjacencyMap, key, word):
    if(existenceMap[key] == False):
        value = False
        if(key == word):
            value = True
        
        adjacencyMap[key] = existenceMap[key] = value

        #if(re.match(key, word, re.IGNORECASE) != None):
         #  adjacencyMap[key] = existenceMap[key] = True 
        
    return existenceMap, adjacencyMap

def checkWindowExistence(existenceMap, key, word):
    if(existenceMap[key] == False):
        existenceMap[key] = re.match(key, word, re.IGNORECASE) 
    return existenceMap

def processWindow(stats, windowText):
    windowExistMap = dict()
    windowExistMap = initializeExistenceMap(windowExistMap)
  
    for word in windowText:
        windowExistMap = checkWindowExistence(windowExistMap, "strong", word)
        windowExistMap = checkWindowExistence(windowExistMap, "powerful", word)
        windowExistMap = checkWindowExistence(windowExistMap, "butter", word)
        windowExistMap = checkWindowExistence(windowExistMap, "salt", word)
        windowExistMap = checkWindowExistence(windowExistMap, "church", word)
        windowExistMap = checkWindowExistence(windowExistMap, "james", word)
        windowExistMap = checkWindowExistence(windowExistMap, "washington", word)

    for word in windowText:
        checkAndUpdateWindowHash(stats, word, windowExistMap, "strong")

def processPage(workername, stats):
    stats.pageCount = stats.pageCount + 1
   
    #Initialize existence map
    existenceMap = dict()
    existenceMap = initializeExistenceMap(existenceMap)

    adjacencyMap = dict()
    adjacencyMap = initializeExistenceMap(adjacencyMap)
    
    #Initialize window variable
    windowText = []
    #Text processing in page
    words = re.split(" ", stats.pageText)
    cleanedwords = []
    for i in range(0, len(words) - 1):
        word = words[i].translate(None, string.punctuation).strip().lower()
        if(word != ""):
            cleanedwords.append(word)
        else:
            continue
        
        if(stats.globalWordHash.has_key(word)):
            stats.globalWordHash[word] = stats.globalWordHash[word] + 1
        else:
            stats.globalWordHash[word] = 1
   
        if(len(windowText) == 20 or i == len(words)-1):
            processWindow(stats, windowText)
            del windowText[:]
        else:
            windowText.append(word)

        checkAndUpdateAdjacency(stats, word, adjacencyMap, "strong")
        adjacencyMap = initializeExistenceMap(adjacencyMap)
        existenceMap, adjacencyMap = checkExistence(existenceMap, adjacencyMap, "strong", word)
        existenceMap, adjacencyMap = checkExistence(existenceMap, adjacencyMap, "powerful", word)
        existenceMap, adjacencyMap = checkExistence(existenceMap, adjacencyMap, "salt", word)
        existenceMap, adjacencyMap = checkExistence(existenceMap, adjacencyMap, "butter", word)
        existenceMap, adjacencyMap = checkExistence(existenceMap, adjacencyMap, "james", word)
        existenceMap, adjacencyMap = checkExistence(existenceMap, adjacencyMap, "church", word)
        existenceMap, adjacencyMap = checkExistence(existenceMap, adjacencyMap, "powerful", word)


    stats.pageLengthList.append(len(words))
    stats.wordCount = stats.wordCount + len(words)

    #Unique words in Page specific processing
    wordSet = set(cleanedwords)

    for word in wordSet:
        word = word.translate(None, string.punctuation)
       
        #Check normal word hash
        checkAndUpdate(stats, "normal", word)
        checkAndUpdate(stats, "strong", word)
    
    stats.bookWordSet.update(wordSet)
    stats.pageUniqueLengthList.append(len(wordSet))
    stats.bookUniqueLength = stats.bookUniqueLength + len(wordSet)

    stats.pageText = ""    


