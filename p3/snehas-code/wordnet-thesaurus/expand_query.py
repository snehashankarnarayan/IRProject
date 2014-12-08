#!/usr/bin/python

'''galago doc --index=/phoenix/ir_code/galago-index-rb4/ --id=FBIS4-20375 --text=true --metadata=false --tokenize=true | sed -n '/Term vector:/,/<TEXT>/p' > output'''

from stopwords import *
from run_galago import *
from collections import Counter
from pprint import pprint
import subprocess
import math
from textblob import Word
from textblob.wordnet import NOUN

expanded_query_terms = dict()
def get_similar_words(cleaned_query_words, doc):
    global expanded_query_terms
    try:
        command = "/home/sneha/phoenix/galago/galago-3.6-bin/bin/galago doc --index=/phoenix/ir_code/galago-index-rb4/ --id=" + doc + " --text=true --metadata=false --tokenize=true | sed -n '/Term vector:/,/<TEXT>/p'"
        outl = subprocess.check_output(command, shell=True) 
        out = outl.split('\n')
        word_array = list()
        for i in range(1, len(out) - 2):
            words = out[i].split()
            if(len(words) > 0):
                word_array.append(words[len(words)-1])
       
        q_syn_list = list()
        for q in cleaned_query_words:
            q_wn = Word(q)
            q_syn_list.append(q_wn.get_synsets(NOUN))

        for w in word_array:
            if w not in cleaned_query_words:
                w_wn = Word(w)
                w_syn = w_wn.get_synsets(NOUN)
                for q_syn in q_syn_list:
                    max_syn = 0
                    for i in range(0, min(2, len(q_syn))):
                        for j in range(0, min(2, len(w_syn))):
                            syn = q_syn[i].path_similarity(w_syn[j])
                            max_syn = max(max_syn, syn)
                    if(max_syn > 0.3):
                        expanded_query_terms[w] = max_syn
    except:
        pass
    print "Done processing " + doc

def expand_query(query, query_no):
    #Some initializations
    global expanded_query_terms
    
    new_list = list()
    expanded_query_terms = dict()
   
    try:
        docs = run_galago(query, query_no)
        query_words = query.split()
        cleaned_query_words = list()
        for word in query_words:
            if word not in stopwords:
                cleaned_query_words.append(word)
        
        for doc in docs:
            try:
                get_similar_words(cleaned_query_words, doc)
            except:
                pass

        count = 0
        for w in sorted(expanded_query_terms, key = expanded_query_terms.__getitem__, reverse = True):
            new_list.append(w)
            count += 1
            if(count == 6):
                break
    except:
        pass
    return new_list
    
