#!/usr/bin/python

import os
import json
import subprocess

def make_json(query, query_no):
    fp = open("my_queries.json", "w")
    queryList = list()
    queryElement = dict()
    queryElement["number"] = query_no
    queryElement["text"] = query
    queryList.append(queryElement)
    fulljson = dict()
    fulljson["queries"] = queryList
    fp.write(json.dumps(fulljson))
    fp.close()
    return True

def run_galago(query, query_no):
    if(make_json(query, query_no)):
        filename = ""
        command = '/home/sneha/phoenix/galago/galago-3.6-bin/bin/galago batch-search --index=/phoenix/ir_code/galago-index-books/ --requested=50 my_queries.json | cut -d" " -f3'
        outl = subprocess.check_output(command, shell=True) 
        out = outl.split('\n')
    return out
