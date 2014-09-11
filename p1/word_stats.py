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

def word_stats(dirName):
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

if __name__ == "__main__":

    t1 = time()
    if sys.argv[1] == "tiny":
        word_stats(tinyDirName)
    elif sys.argv[1] == "small":
        word_stats(smallDirName)
    elif sys.argv[1] == "medium":
        word_stats(mediumDirName)
    elif sys.argv[1] == "big":
        word_stats(bigDirName)
    t2 = time()
    print 'Time taken in seconds: %f' %(t2-t1)
