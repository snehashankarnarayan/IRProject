#!/usr/bin/python

import xml.etree.cElementTree as ET
from os import listdir
import re
import sys
from time import time
import string
from collections import Counter
from sets import Set

#Constants
tinyDirName = "/phoenix/ir_code/data/books-tiny/"
mediumDirName = "/phoenix/ir_code/data/books-medium/"
smallDirName = "/phoenix/ir_code/data/books-small/"
bigDirName = "/phoenix/ir_code/data/books-big/"

#Globals
wordCount = 0
pageCount = 0
pageText = ""

#Global hashtables/dictionaries
globalWordHash = Counter()
bookWordHash = Counter()
pageWordHash = Counter()

#Per book sets
bookWordSet = Set()

def getFileList(rootDirName):
    tinyDir =  listdir(rootDirName);
    fileList = []
    for dirName in tinyDir:
        xmlFiles = listdir(rootDirName + dirName)
        for xmlFile in xmlFiles:
            fileList.append(rootDirName + dirName + "/" + xmlFile)
    return fileList

def processPage():
    global pageCount
    global globalWordHash
    global pageText
    global bookWordSet
    pageCount = pageCount + 1
    
    #Text processing in page
    words = re.split(" ", pageText)
    for( i = 0; i < len(words); i++):
        words[i] = words[i].translate(None, string.punctuation)

        if(globalWordHash.has_key(word)):
            globalWordHash[word] = globalWordHash[word] + 1
        else:
            globalWordHash[word] = 1
    
    #Page specific processing
    wordSet = set(words)
    for word in wordSet:
        word = word.translate(None, string.punctuation)
        if(pageWordHash.has_key(word)):
            pageWordHash[word] = pageWordHash[word] + 1
        else:
            pageWordHash[word] = 1
    
    bookWordSet.update(wordSet)
    #sys.exit(0)



def processFile(fileName):
    global pageText
    global bookWordHash
    global bookWordSet
    bookWordSet.clear()
    for event, elem in ET.iterparse(fileName):
        if (elem.tag == "page" and event == 'start'):
            pageText = " "
        if(elem.tag == "line" and event == 'end' and elem.text != None):
            pageText = pageText + " " + elem.text
        if(elem.tag == "page" and event == 'end'):
            processPage()
        elem.clear() 

    #Update book hash
    for word in bookWordSet:
        if(bookWordHash.has_key(word)):
            bookWordHash[word] = bookWordHash[word] + 1
        else:
            bookWordHash[word] = 1
    

def processDirectory(dirName):
    fileList = getFileList(dirName)
    for fileName in fileList:
        try:
            processFile(fileName)
        except xml.etree.ElementTree.ParseError:
            print "Parse Error"
            pass        
        except (RuntimeError, TypeError, NameError):
            continue
            pass
        except:
            print "Unexpected Error.. Continue anyway"
            pass

def testMe():
    fileList = getFileList(tinyDirName)
    processFile(fileList[0])
    print "WordCount " + str(wordCount)
    print "PageCount " + str(pageCount)
    print "GlobalWordHash"
    print globalWordHash
    print "pageWordHash"
    print pageWordHash
    print "BookWordHash"
    print bookWordHash

if __name__ == "__main__":
    t1 = time()
    if sys.argv[1] == "test":
        testMe()
    elif sys.argv[1] == "tiny":
        processDirectory(tinyDirName)
    elif sys.argv[1] == "small":
        processDirectory(smallDirName)
    elif sys.argv[1] == "medium":
        processDirectory(mediumDirName)
    elif sys.argv[1] == "big":
        processDirectory(bigDirName)
    t2 = time()
    print 'Time taken in seconds: %f' %(t2-t1)
