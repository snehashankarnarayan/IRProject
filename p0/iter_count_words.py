#!/usr/bin/python

import xml.etree.cElementTree as ET
from os import listdir
import re
import sys
from time import time

#Constants
tinyDirName = "/phoenix/ir_code/data/books-tiny/"
mediumDirName = "/phoenix/ir_code/data/books-medium/"
smallDirName = "/phoenix/ir_code/data/books-small/"
bigDirName = "/phoenix/ir_code/data/books-big/"

#Globals
global wordCount;

def countString(text):
    global wordCount
    words = re.split(" ", text)
    wordCount += len(words)
    return len(words)

def getFileList(rootDirName):
    tinyDir =  listdir(rootDirName);
    fileList = []
    for dirName in tinyDir:
        xmlFiles = listdir(rootDirName + dirName)
        for xmlFile in xmlFiles:
            fileList.append(rootDirName + dirName + "/" + xmlFile)
    return fileList

def processFile(fileName):
    for event, elem in ET.iterparse(fileName):
        if event == 'end':
            if(elem.text != None):
                countString(elem.text)
        elem.clear() 

def count_words(dirName):
    global wordCount
    wordCount = 0
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
    print "Final wordcount:" + str(wordCount)

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
    print 'Time taken in seconds: %f' %(t2-t1)
