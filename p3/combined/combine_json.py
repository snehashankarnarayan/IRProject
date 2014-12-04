#!/usr/bin/python

import json
import sys
from pprint import pprint



def unique_list(l):
        ulist = list()
        [ulist.append(x) for x in l if x not in ulist]
        return ulist

fp1 = open(sys.argv[1], "r")
fp2 = open(sys.argv[2], "r")

outfile = open(sys.argv[3], "w")
json1 = json.load(fp1)
json2 = json.load(fp2)

q1_list = json1.get("queries")
q2_list = json2.get("queries")

queryList = list()
for i in range(0, min(len(q1_list), len(q2_list))):
    q1 = q1_list[i].get("text")
    q2 = q2_list[i].get("text")

    queryElement = dict()
    queryElement["number"] = q1_list[i].get("number")
    a = q1 + " " + q2
    queryElement["text"] = ' '.join(unique_list(a.split()))
    queryList.append(queryElement)

fulljson = dict()
fulljson["queries"] = queryList
outfile.write(json.dumps(fulljson))
outfile.close()
fp1.close()
fp2.close()

