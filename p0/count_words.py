#!/usr/bin/python

import xml.etree.ElementTree as ET
from os import listdir
import re

#Constants
tinyRootName = "/phoenix/ir_code/data/books-small/"
smallRootName = "/phoenix/ir_code/data/books-small/"

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

def count_words():
    global wordCount
    wordCount = 0
   
    fileList = getFileList(tinyRootName)
    for fileName in fileList:
        parseFile(fileName)
        print wordCount
    print wordCount


if __name__ == "__main__":
    count_words()
