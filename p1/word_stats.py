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
bookCount = 0
pageText = ""

bookLengthList = []
pageLengthList = []

bookUniqueLengthList = []
pageUniqueLengthList = []

bookLength = 0

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
    global pageLengthList
    global pageLengthUniqueList
    global bookLength
    global bookUniqueLength
    pageCount = pageCount + 1
    
    #Text processing in page
    words = re.split(" ", pageText)
    for i in range(0, len(words) - 1):
        words[i] = words[i].translate(None, string.punctuation)

        if(globalWordHash.has_key(words[i])):
            globalWordHash[words[i]] = globalWordHash[words[i]] + 1
        else:
            globalWordHash[words[i]] = 1
    
    pageLengthList.append(len(words))
    bookLength = bookLength + len(words)
    #Page specific processing
    wordSet = set(words)
    for word in wordSet:
        word = word.translate(None, string.punctuation)
        if(pageWordHash.has_key(word)):
            pageWordHash[word] = pageWordHash[word] + 1
        else:
            pageWordHash[word] = 1
    
    bookWordSet.update(wordSet)
    pageUniqueLengthList.append(len(wordSet))
    bookUniqueLength = bookUniqueLength + len(wordSet)




def processFile(fileName):
    global pageText
    global bookWordHash
    global bookWordSet
    global bookCount
    global bookLength
    global bookUniqueLength
    global bookLengthList
    global bookUniqueLengthList

    bookLength = 0
    bookUniqueLength = 0
    bookCount = bookCount + 1
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

    bookLengthList.append(bookLength)
    bookUniqueLengthList.append(bookUniqueLength)
    

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
    print bookLengthList
    print pageLengthList

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
