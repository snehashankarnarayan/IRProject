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
trecFileName = "trec"
trecExtension = ".dat"

def getFileList(rootDirName):
    tinyDir =  listdir(rootDirName);
    fileList = []
    for dirName in tinyDir:
        xmlFiles = listdir(rootDirName + dirName)
        for xmlFile in xmlFiles:
            fileList.append(rootDirName + dirName + "/" + xmlFile)
    return fileList

def getOutFile(dirName, count):
    dirName = dirName[:len(dirName)-1]
    filename = dirName + "-trec/" + trecFileName + "_" + str(count) + trecExtension
    return filename

def getPageID(fileName):
    parts = fileName.split('/')
    pageId = parts[len(parts) - 1]
    pageId = pageId[:len(pageId) - 10]
    return pageId



def processPage(pageText, fp, fileName, pageCount):
    pageId = getPageID(fileName) + "-" + pageCount
    lines = []
    line = "<DOC>\n<DOCNO>" + pageId + "</DOCNO>\n<TEXT>"
    lines.append(line)
    lines.append(pageText)
    line = "</TEXT>\n</DOC>\n"
    lines.append(line)
    fp.writelines(lines)

def processFile(fileName, fp):
    pageText = ""
    pageCount = ""
    for event, elem in ET.iterparse(fileName):
        if(elem.tag == "line" and event == "end" and elem.text != None):
            pageText = pageText + " " + elem.text
        if(elem.tag == "page" and event == "end"):
            pageText = pageText.strip()
            attrib = elem.attrib
            pageCount = attrib["id"]
            if(len(pageText) > 0):
                processPage(pageText, fp, fileName, pageCount)
                pageText = ""
        elem.clear() 

def make_trec(dirName):
    fileList = getFileList(dirName)
    count = 0
    outfile = getOutFile(dirName, count)
    fp = open(outfile, "w")
    print "No of files: " + str(len(fileList))
    for i in range(0, len(fileList)):
        if(i%100 == 0 and i != 0):
            fp.close()
            count += 1
            outfile = getOutFile(dirName, count)
            fp = open(outfile, "w")
        filename = fileList[i]
        print "Processing..." + filename
        processFile(filename, fp)

if __name__ == "__main__":

    t1 = time()
    if sys.argv[1] == "tiny":
        make_trec(tinyDirName)
    elif sys.argv[1] == "small":
        make_trec(smallDirName)
    elif sys.argv[1] == "medium":
        make_trec(mediumDirName)
    elif sys.argv[1] == "big":
        make_trec(bigDirName)
    t2 = time()
    print 'Time taken in seconds: %f' %(t2-t1)
