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
from process_book import processFile

def getFileList(rootDirName):
    tinyDir =  listdir(rootDirName);
    fileList = []
    for dirName in tinyDir:
        xmlFiles = listdir(rootDirName + dirName)
        for xmlFile in xmlFiles:
            fileList.append(rootDirName + dirName + "/" + xmlFile)
    return fileList

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
    fileList = getFileList(stats.tinyDirName)
    processFile(fileList[0])
    print "WordCount " + str(stats.wordCount)
    print "PageCount " + str(stats.pageCount)
    print stats.bookLengthList
    print stats.pageLengthList
    print stats.bookUniqueLengthList
    print stats.pageUniqueLengthList

if __name__ == "__main__":
    t1 = time()
    if sys.argv[1] == "test":
        testMe()
    elif sys.argv[1] == "tiny":
        processDirectory(stats.tinyDirName)
    elif sys.argv[1] == "small":
        processDirectory(stats.smallDirName)
    elif sys.argv[1] == "medium":
        processDirectory(stats.mediumDirName)
    elif sys.argv[1] == "big":
        processDirectory(stats.bigDirName)
    t2 = time()
    print 'Time taken in seconds: %f' %(t2-t1)
