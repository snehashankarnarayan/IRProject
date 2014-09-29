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

def checkAndUpdatePageStats(stats, key, word, eMap):
    if(key == "normal"):
        if(stats.pageWordHash.has_key(word)):
            stats.pageWordHash[word] = stats.pageWordHash[word] + 1
        else:
            stats.pageWordHash[word] = 1
    
    elif(eMap[key] == True):
        if(key == "strong" and word not in stopwords and word != "strong"):
            if(stats.strongHash.has_key(word)):
                stats.strongHash[word] = stats.strongHash[word] + 1
            else:
                stats.strongHash[word] = 1
    
        elif(key == "powerful" and word not in stopwords and word != "powerful"):
            if(stats.powerfulHash.has_key(word)):
                stats.powerfulHash[word] = stats.powerfulHash[word] + 1
            else:
                stats.powerfulHash[word] = 1

        elif(key == "james" and word not in stopwords and word != "james"):
            if(stats.jamesHash.has_key(word)):
                stats.jamesHash[word] = stats.jamesHash[word] + 1
            else:
                stats.jamesHash[word] = 1

        elif(key == "salt" and word not in stopwords and word != "salt"):
            if(stats.saltHash.has_key(word)):
                stats.saltHash[word] = stats.saltHash[word] + 1
            else:
                stats.saltHash[word] = 1

        elif(key == "butter" and word not in stopwords and word != "butter"):
            if(stats.butterHash.has_key(word)):
                stats.butterHash[word] = stats.butterHash[word] + 1
            else:
                stats.butterHash[word] = 1

        elif(key == "washington" and word not in stopwords and word != "washington"):
            if(stats.washingtonHash.has_key(word)):
                stats.washingtonHash[word] = stats.washingtonHash[word] + 1
            else:
                stats.washingtonHash[word] = 1

        elif(key == "church" and word not in stopwords and word != "church"):
            if(stats.churchHash.has_key(word)):
                stats.churchHash[word] = stats.churchHash[word] + 1
            else:
                stats.churchHash[word] = 1


def checkAndUpdateAdjacency(stats, word, eMap, key): 
    if(eMap[key] == True):
        if(key == "strong" and word not in stopwords):
            if(stats.strongAdjacentHash.has_key(word)):
                stats.strongAdjacentHash[word] = stats.strongAdjacentHash[word] + 1
            else:
                stats.strongAdjacentHash[word] = 1
        
        elif(key == "powerful" and word not in stopwords):
            if(stats.powerfulAdjacentHash.has_key(word)):
                stats.powerfulAdjacentHash[word] = stats.powerfulAdjacentHash[word] + 1
            else:
                stats.powerfulAdjacentHash[word] = 1

        elif(key == "salt" and word not in stopwords):
            if(stats.saltAdjacentHash.has_key(word)):
                stats.saltAdjacentHash[word] = stats.saltAdjacentHash[word] + 1
            else:
                stats.saltAdjacentHash[word] = 1

        elif(key == "butter" and word not in stopwords):
            if(stats.butterAdjacentHash.has_key(word)):
                stats.butterAdjacentHash[word] = stats.butterAdjacentHash[word] + 1
            else:
                stats.butterAdjacentHash[word] = 1

        elif(key == "james" and word not in stopwords):
            if(stats.jamesAdjacentHash.has_key(word)):
                stats.jamesAdjacentHash[word] = stats.jamesAdjacentHash[word] + 1
            else:
                stats.jamesAdjacentHash[word] = 1

        elif(key == "church" and word not in stopwords):
            if(stats.churchAdjacentHash.has_key(word)):
                stats.churchAdjacentHash[word] = stats.churchAdjacentHash[word] + 1
            else:
                stats.churchAdjacentHash[word] = 1

        elif(key == "washington" and word not in stopwords):
            if(stats.washingtonAdjacentHash.has_key(word)):
                stats.washingtonAdjacentHash[word] = stats.washingtonAdjacentHash[word] + 1
            else:
                stats.washingtonAdjacentHash[word] = 1


def checkAndUpdateWindowHash(stats, word, eMap, key): 
    if(eMap[key] == True):
        if(key == "strong" and word not in stopwords and word != "strong"):
            if(stats.strongWindowHash.has_key(word)):
                stats.strongWindowHash[word] = stats.strongWindowHash[word] + 1
            else:
                stats.strongWindowHash[word] = 1
        
        elif(key == "powerful" and word not in stopwords and word != "powerful"):
            if(stats.powerfulWindowHash.has_key(word)):
                stats.powerfulWindowHash[word] = stats.powerfulWindowHash[word] + 1
            else:
                stats.powerfulWindowHash[word] = 1
        
        elif(key == "salt" and word not in stopwords and word != "salt"):
            if(stats.saltWindowHash.has_key(word)):
                stats.saltWindowHash[word] = stats.saltWindowHash[word] + 1
            else:
                stats.saltWindowHash[word] = 1
    
        elif(key == "butter" and word not in stopwords and word != "butter"):
            if(stats.butterWindowHash.has_key(word)):
                stats.butterWindowHash[word] = stats.butterWindowHash[word] + 1
            else:
                stats.butterWindowHash[word] = 1
    
        elif(key == "james" and word not in stopwords and word != "james"):
            if(stats.jamesWindowHash.has_key(word)):
                stats.jamesWindowHash[word] = stats.jamesWindowHash[word] + 1
            else:
                stats.jamesWindowHash[word] = 1
    
        elif(key == "church" and word not in stopwords and word != "church"):
            if(stats.churchWindowHash.has_key(word)):
                stats.churchWindowHash[word] = stats.churchWindowHash[word] + 1
            else:
                stats.churchWindowHash[word] = 1
        
        elif(key == "washington" and word not in stopwords and word != "washington"):
            if(stats.washingtonWindowHash.has_key(word)):
                stats.washingtonWindowHash[word] = stats.washingtonWindowHash[word] + 1
            else:
                stats.washingtonWindowHash[word] = 1
    
def initializeExistenceMap(exist):
    exist["strong"] = False
    exist["powerful"] = False
    exist["salt"] = False
    exist["butter"] = False
    exist["james"] = False
    exist["church"] = False
    exist["washington"] = False
    return exist

def checkExistenceAndPrecedence(stats, existenceMap, key, word, PrecedingWord):
    value = False
    if(key == word):
        value = True
        existenceMap[key] = value
   
    if(value == True and PrecedingWord != None):
        if(key == "james" and PrecedingWord not in stopwords):
            if(stats.jamesPrecedingHash.has_key(PrecedingWord)):
                stats.jamesPrecedingHash[PrecedingWord] = stats.jamesPrecedingHash[PrecedingWord] + 1
            else:
                stats.jamesPrecedingHash[PrecedingWord] = 1
    
        elif(key == "church" and PrecedingWord not in stopwords):
            if(stats.churchPrecedingHash.has_key(PrecedingWord)):
                stats.churchPrecedingHash[PrecedingWord] = stats.churchPrecedingHash[PrecedingWord] + 1
            else:
                stats.churchPrecedingHash[PrecedingWord] = 1
        
        elif(key == "washington" and PrecedingWord not in stopwords):
            if(stats.washingtonPrecedingHash.has_key(PrecedingWord)):
                stats.washingtonPrecedingHash[PrecedingWord] = stats.washingtonPrecedingHash[PrecedingWord] + 1
            else:
                stats.washingtonPrecedingHash[PrecedingWord] = 1
    
    return existenceMap

def checkExistence(existenceMap, key, word):
    if(existenceMap[key] == False):
        value = False
        if(key == word):
            value = True
        existenceMap[key] = value

    return existenceMap

def processWindow(stats, windowText):
    windowExistMap = dict()
    windowExistMap = initializeExistenceMap(windowExistMap)
  
    for word in windowText:
        windowExistMap = checkExistence(windowExistMap, "strong", word)
        windowExistMap = checkExistence(windowExistMap, "powerful", word)
        windowExistMap = checkExistence(windowExistMap, "butter", word)
        windowExistMap = checkExistence(windowExistMap, "salt", word)
        windowExistMap = checkExistence(windowExistMap, "church", word)
        windowExistMap = checkExistence(windowExistMap, "james", word)
        windowExistMap = checkExistence(windowExistMap, "washington", word)

    for word in windowText:
        checkAndUpdateWindowHash(stats, word, windowExistMap, "strong")
        checkAndUpdateWindowHash(stats, word, windowExistMap, "powerful")
        checkAndUpdateWindowHash(stats, word, windowExistMap, "butter")
        checkAndUpdateWindowHash(stats, word, windowExistMap, "salt")
        checkAndUpdateWindowHash(stats, word, windowExistMap, "church")
        checkAndUpdateWindowHash(stats, word, windowExistMap, "james")
        checkAndUpdateWindowHash(stats, word, windowExistMap, "washington")

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
    precedingWord = None
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
        checkAndUpdateAdjacency(stats, word, adjacencyMap, "powerful")
        checkAndUpdateAdjacency(stats, word, adjacencyMap, "salt")
        checkAndUpdateAdjacency(stats, word, adjacencyMap, "butter")
        checkAndUpdateAdjacency(stats, word, adjacencyMap, "james")
        checkAndUpdateAdjacency(stats, word, adjacencyMap, "church")
        checkAndUpdateAdjacency(stats, word, adjacencyMap, "washington")
        
        #Clear map for next round
        adjacencyMap = initializeExistenceMap(adjacencyMap)
        
        #Deal with existence and precedence
        existenceMap = checkExistenceAndPrecedence(stats, existenceMap, "strong", word, precedingWord)
        existenceMap = checkExistenceAndPrecedence(stats, existenceMap, "powerful", word, precedingWord)
        existenceMap = checkExistenceAndPrecedence(stats, existenceMap, "salt", word, precedingWord)
        existenceMap = checkExistenceAndPrecedence(stats, existenceMap, "butter", word, precedingWord)
        existenceMap = checkExistenceAndPrecedence(stats, existenceMap, "james", word, precedingWord)
        existenceMap = checkExistenceAndPrecedence(stats, existenceMap, "church", word, precedingWord)
        existenceMap = checkExistenceAndPrecedence(stats, existenceMap, "washington", word, precedingWord)

        #Deal with adjacency
        adjacencyMap = checkExistence(adjacencyMap, "strong", word)
        adjacencyMap = checkExistence(adjacencyMap, "powerful", word)
        adjacencyMap = checkExistence(adjacencyMap, "salt", word)
        adjacencyMap = checkExistence(adjacencyMap, "butter", word)
        adjacencyMap = checkExistence(adjacencyMap, "james", word)
        adjacencyMap = checkExistence(adjacencyMap, "church", word)
        adjacencyMap = checkExistence(adjacencyMap, "washington", word)
        
        precedingWord = word
        
    stats.pageLengthList.append(len(words))
    stats.wordCount = stats.wordCount + len(words)

    #Unique words in Page specific processing
    wordSet = set(cleanedwords)

    for word in wordSet:
        word = word.translate(None, string.punctuation)
       
        #Check normal word hash
        checkAndUpdatePageStats(stats, "normal", word, existenceMap)
        checkAndUpdatePageStats(stats, "strong", word, existenceMap)
        checkAndUpdatePageStats(stats, "powerful", word, existenceMap)
        checkAndUpdatePageStats(stats, "salt", word, existenceMap)
        checkAndUpdatePageStats(stats, "butter", word, existenceMap)
        checkAndUpdatePageStats(stats, "james", word, existenceMap)
        checkAndUpdatePageStats(stats, "washington", word, existenceMap)
        checkAndUpdatePageStats(stats, "church", word, existenceMap)
    
    stats.bookWordSet.update(wordSet)
    stats.pageUniqueLengthList.append(len(wordSet))
    
    #print "unique: " +  str(len(wordSet)) + " wordcount " + str(len(words))
    
    stats.pageText = ""    


