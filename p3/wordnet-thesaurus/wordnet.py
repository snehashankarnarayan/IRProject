#!/usr/bin/python

from textblob import Word
from textblob.wordnet import NOUN
from textblob.wordnet import VERB
p = Word("plant", NOUN)
q = Word("obviously", VERB)

print q

psyn = p.get_synsets(NOUN)
qsyn = q.get_synsets(NOUN)

print qsyn
max_syn = 0
for i in psyn:
    for j in qsyn:
        syn = i.path_similarity(j)
        if(syn > max_syn):
            max_syn = syn

print max_syn

