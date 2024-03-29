#!/usr/bin/python

import xml.etree.ElementTree as ET
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

def countDict(attrib):
    global wordCount
    wordCount += len(attrib) * 2
    print attrib

def countString(text):
    global wordCount
    words = re.split(" ", text)
    wordCount += len(words)
    return len(words)

def processNode(root):
    #if(root.attrib != None):
    #    countDict(root.attrib)
    if(root.text != None):
        countString(root.text)
    for child in root:
        processNode(child)

def parseFile(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot();
    processNode(root)

def getFileList(rootDirName):
    tinyDir =  listdir(rootDirName);
    fileList = []
    for dirName in tinyDir:
        xmlFiles = listdir(rootDirName + dirName)
        for xmlFile in xmlFiles:
            fileList.append(rootDirName + dirName + "/" + xmlFile)
    return fileList

def count_words(dirName):
    try:
        global wordCount
        wordCount = 0
        fileList = getFileList(dirName)
        for fileName in fileList:
            print wordCount
            try:
                parseFile(fileName)
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
    except:
        pass



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
