#!/usr/bin/python

import xml.etree.cElementTree as ET
from os import listdir
import re
from pprint import pprint
import sys
from time import time
import json

def processFile(fileName):
    split = fileName.split('.')
    outfile =  "queries-robust.json"
    fp = open(outfile, "w")
    
    queryList = []
   
    for event, elem in ET.iterparse(fileName):
        if(elem.tag == "title" and event == "end" and elem.text != None):
            title = elem.text.strip()
        if(elem.tag == "num" and event == "end"):
            query_no = elem.text.strip()
        if(elem.tag == "topic" and event == "end"):
            queryElement = dict()
            queryElement["number"] = query_no
            queryElement["text"] = title
            queryList.append(queryElement)
        elem.clear() 

    fulljson = dict()
    fulljson["queries"] = queryList
    pprint(fulljson)
    fp.write(json.dumps(fulljson))
    fp.close()

if __name__ == "__main__":

    t1 = time()
    processFile(sys.argv[1])
    t2 = time()
    print 'Time taken in seconds: %f' %(t2-t1)
