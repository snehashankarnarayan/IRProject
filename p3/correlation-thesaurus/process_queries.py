#!/usr/bin/python

from expand_query import *
import xml.etree.cElementTree as ET
import json

def process_queries(fileName):
    split = fileName.split('.')
    outfile =  split[0] + ".json"
    fp = open(outfile, "w")
    tempfile = open(split[0] + "_temp.txt", "w") 
    in_queryList = list()
    out_queryList = list()
   
    for event, elem in ET.iterparse(fileName):
        if(elem.tag == "title" and event == "end" and elem.text != None):
            title = elem.text.strip()
        if(elem.tag == "num" and event == "end"):
            query_no = elem.text.strip()
        if(elem.tag == "topic" and event == "end"):
            queryElement = dict()
            queryElement["number"] = query_no
            queryElement["text"] = title
            in_queryList.append(queryElement)
        elem.clear() 
    
    for item in in_queryList:
        out_entity = item
        term_list = expand_query(item["text"], item["number"])
        new_query = ""
        for w in term_list:
            new_query = new_query + " " + w
        out_entity["text"] = out_entity["text"] + " " + new_query
        tempfile.write(out_entity["number"] + ":" + out_entity["text"] + '\n')
        out_queryList.append(out_entity)

    fulljson = dict()
    fulljson["queries"] = out_queryList
    fp.write(json.dumps(fulljson))
    fp.close()
    tempfile.close()
