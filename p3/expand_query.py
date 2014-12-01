#!/usr/bin/python

'''galago doc --index=/phoenix/ir_code/galago-index-rb4/ --id=FBIS4-20375 --text=true --metadata=false --tokenize=true | sed -n '/Term vector:/,/<TEXT>/p' > output'''

from stopwords import *
from run_galago import *
from collections import Counter
from pprint import pprint
import subprocess
import math

word_dict = dict()
query_word_counter = Counter()
cor_word_counter = Counter()
vocab_length = 0

def get_correlated_words(cleaned_query_words, doc):
    global word_dict
    global query_word_counter
    global cor_word_counter
    global vocab_length
    
    command = "/home/sneha/phoenix/galago/galago-3.6-bin/bin/galago doc --index=/phoenix/ir_code/galago-index-rb4/ --id=" + doc + " --text=true --metadata=false --tokenize=true | sed -n '/Term vector:/,/<TEXT>/p'"
    outl = subprocess.check_output(command, shell=True) 
    out = outl.split('\n')
    word_array = list()
    for i in range(1, len(out) - 2):
        words = out[i].split()
        if(len(words) > 0):
            word_array.append(words[len(words)-1])
   
    vocab_length += len(word_array)

    for word in cleaned_query_words:
        ct = Counter()
        query_word_counter[word] = query_word_counter[word] + word_array.count(word)
        try:
            index = word_array.index(word, 0)
            while(True):
                if(index != 0):
                    st = word_array[index - 1]
                    if st not in stopwords:
                        ct[st] = 1
                if(index+1 != len(word_array)):
                    st = word_array[index + 1]
                    if st not in stopwords:
                        ct[st] = 1
                index = word_array.index(word, index + 1)
        except ValueError:
            pass

        count = word_dict.get(word)
        count.update(ct)
        word_dict[word] = count

    for word in cleaned_query_words:
        counter_words = word_dict[word].keys()
        for w in counter_words:
            cor_word_counter[w] = cor_word_counter[w] + word_array.count(w)
    
    print "Done processing " + doc

def expand_query(query, query_no):
    global word_dict
    docs = run_galago(query, query_no)
    query_words = query.split()
    cleaned_query_words = list()
    for word in query_words:
        if word not in stopwords:
            cleaned_query_words.append(word)
            word_dict[word] = Counter()
    
    for doc in docs:
        get_correlated_words(cleaned_query_words, doc)

    expanded_query_terms = list()
    
    #Some terminologies
    #p_t = Probability of query term = count(query_term)/vocab_length
    #p_c = Probability of correlated term = count(cor_term)/vocab_length
    #p_ct = prob(query term with cor term) = count(cor_term W/ query term)/count(query term)
    #i_ct = log(p_ct/p_c.p_t)
    #word_dict = dict(); query_word_counter = Counter(); cor_word_counter = Counter(); vocab_length = 0
    for word in cleaned_query_words:
        word_dict_counts = word_dict[word]

        p_t = query_word_counter[word] * 1.0 / vocab_length
        
        cor_word_list = word_dict_counts.keys()

        i_ct_list = dict()
        for c in cor_word_list:
            p_c = cor_word_counter[c] * 1.0 / vocab_length
            p_ct = word_dict_counts[c] * 1.0 / query_word_counter[word]
            i_ct = math.log(p_ct/(p_c * p_t))
            i_ct_list[c] = i_ct
        
        i_ct_values = i_ct_list.values()
        max_ict = max(i_ct_values)
        min_ict = min(i_ct_values)

        for c in cor_word_list:
            i_ct_list[c] = (i_ct_list[c] - min_ict)/(max_ict - min_ict)
            if(i_ct_list[c] <= 0.5):
                if c not in cleaned_query_words:
                    expanded_query_terms.append(c)
        #for w in sorted(i_ct_list, key = i_ct_list.__getitem__, reverse = False):
    return expanded_query_terms
