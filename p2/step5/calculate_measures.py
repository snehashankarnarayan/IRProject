#!/usr/bin/python

import math
from pprint import pprint
from classes import *
from time import time
import sys

def calculate_measures(filename, args, rang):
    fp = open(filename, "r")
    outfile = open(filename + "-output", "w")
    currentQuery = ""
    queryList = list()
    relList = list()
    queryNumberList = list()
    for line in fp:
        #301 0 FBIS4-21302 1
        words = line.split(" ")
        if(len(words) is (int(args) + 1)):
            if(currentQuery != words[0]):
                #Append current list
                entity = judgements(currentQuery, list(relList))
                queryList.append(entity)
                relList = list()
            currentQuery = words[0]
            relList.append(int(words[int(args)].strip()))

    fp.close()
    
    #Computing average precisions
    avg_list = 0.0
    for item in queryList:
        avg = 0.0    
        rlist = item.rel
        for val in rlist:
            avg += val
        if(len(item.rel) > 0):
            avg = avg/len(item.rel)
        else:
            avg = 0
        avg_list += avg
        outfile.write("AP " + item.query + " " + str(avg) + "\n")
    
    avg_list = avg_list/len(queryList)
    outfile.write("Mean average precision: " + str(avg_list) + "\n")

    #Computing precision at 10
    for item in queryList:
        rlist = item.rel
        precision = 0.0
        i = 0
        while( i < len(rlist) and i < 10):
            relevance = rlist[i]
            if(relevance >= int(rang)):
                precision += 1.0
            i += 1
        precision = precision/10.0
        outfile.write("Precision: " + item.query + " " + str(precision) + "\n")
    
    for item in queryList:
        rlist = list(item.rel)
        #print rlist
        #print item.rel
        slist = list(item.rel)
        slist.sort()
        print slist
        dcg = 0.0
        idcg = 0.0
        i = 0
        while( i < len(rlist) and i < 20):
            j = i+1
            dcg += (pow(2, rlist[i]) - 1)/(math.log(j+1, 2))
            idcg += (pow(2, slist[i]) - 1)/(math.log(j+1, 2))
            i += 1
            #print dcg
            #print idcg
        
        #ndcg = dcg/idcg
        #outfile.write("NDCG: " + item.query + " " + str(ndcg) + "\n")
    '''for item in queryList:
        print item.rel
        rlist = list(item.rel)
        slist = list(item.rel)
        slist.sort()
        print rlist
        print slist
        dcg = 0.0
        idcg = 0.0
        i = 0
        while( i < len(rlist) and i < 20):
            j = i+1
            dcg += (pow(2, rlist[i]) - 1)/(math.log(j+1, 2))
            idcg += (pow(2, slist[i]) - 1)/(math.log(j+1, 2))
            i += 1
        ndcg = dcg/idcg
        outfile.write("NDCG: " + item.query + " " + str(ndcg) + "\n")'''


    outfile.close()

            


        



if __name__ == "__main__":
    t1 = time()
    #Usage: filename, items in one line, precision_range
    calculate_measures(sys.argv[1], sys.argv[2], sys.argv[3])
    t2 = time()
    minutes = (t2 - t1)/60.0
    print 'Time taken in seconds: %f' %(t2-t1)
    print 'Time taken in minutes: ' + str(minutes)
