#!/usr/bin/python

import math
from pprint import pprint
from classes import *
from time import time
import sys

def calculate_measures(filename, rankfilename, rang):
    fp = open(filename, "r")
    rfile = open(rankfilename, "r")
    outfile = open(filename + "-output", "w")
    
    #Processing judgement file
    currentQuery = "none"
    queryList = dict()
    relList = dict()
    for line in fp:
        #301 0 FBIS4-21302 1
        words = line.split(" ")
        if(currentQuery != words[0] and currentQuery != "none"):
            #Append current list
            queryList[currentQuery] = dict(relList)
            relList = dict()
        currentQuery = words[0]
        relList[words[1]] = int(words[2].strip())
    fp.close()

    #Processing ranked list
    #320 Q0 FBIS3-26609 100 -8.88567446 galago
    currentQuery = "none"
    rankList = list()
    relList = list()
    for line in rfile:
        words = line.split(" ")
        if(currentQuery != words[0] and currentQuery != "none"):
            #Append current list
            entity = judgements(currentQuery, list(relList))
            rankList.append(entity)
            relList = list()
        currentQuery = words[0]
        relList.append(words[2])
    rfile.close()
    
    #Compute mean avg precision
    mean_avg = 0.0
    for item in rankList:
        recall = 0
        avg_prec = 0.0
        prec10 = 0.0
        prec10_counter = 1
        qEntity = queryList.get(item.query)
        if(qEntity != None):
            for docID in item.rel:
                relevance = qEntity.get(docID, 0)
                if(relevance >= int(rang)):
                    avg_prec += 1
                    recall += 1
                    if(prec10_counter <= 10):
                        prec10 += 1
                prec10_counter += 1
            if(recall != 0):
                avg_prec = avg_prec/recall
                outfile.write("Avg precision " + item.query + " " + str(avg_prec) + "\n")
                mean_avg += avg_prec
            prec10 = prec10/10
            outfile.write("Precision at 10: " + item.query + " " + str(prec10) + "\n")
    mean_avg = mean_avg/len(rankList)
    outfile.write("Mean Avg precision " + str(mean_avg) + "\n")

    for item in rankList:
        rList = list()
        qEntity = queryList.get(item.query)
        counter = 0
        if(qEntity != None):
            for docID in item.rel:
                relevance = qEntity.get(docID, 0)
                rList.append(relevance)
                counter += 1
                if(counter == 20):
                    break
            sList = list(rList)
            sList.sort()
            dcg = 0.0
            idcg = 0.0
            for i in range(0, len(rList)):
                j = i+1
                dcg += (pow(2, rList[i]) - 1)/(math.log(j+1, 2))
                idcg += (pow(2, sList[i]) - 1)/(math.log(j+1, 2))
            if(idcg > 0):
                ndcg = dcg/idcg
                outfile.write("NDCG: " + item.query + " " + str(ndcg) + "\n")
    
    outfile.close()

if __name__ == "__main__":
    t1 = time()
    #Usage: filename, items in one line, precision_range
    calculate_measures(sys.argv[1], sys.argv[2], sys.argv[3])
    t2 = time()
    minutes = (t2 - t1)/60.0
    print 'Time taken in seconds: %f' %(t2-t1)
    print 'Time taken in minutes: ' + str(minutes)
