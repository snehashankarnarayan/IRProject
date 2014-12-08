#!/usr/bin/python

from time import time

def get_doc_vector():
    fp = open("output", "r")
    lines = fp.readlines()
    word_array = list()
    for i in range(1, len(lines)-2):
        words = lines[i].split()
        word_array.append(words[len(words)-1])

    print word_array

if __name__ == "__main__":
    t1 = time()
    get_doc_vector()
    t2 = time()
    minutes = (t2 - t1)/60.0
    print 'Time taken in seconds: %f' %(t2-t1)
    print 'Time taken in minutes: ' + str(minutes)
