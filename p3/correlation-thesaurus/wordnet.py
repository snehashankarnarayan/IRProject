#!/usr/bin/python

from textblob import Word
from textblob.wordnet import NOUN
word = Word("plant")
print word.get_synsets(NOUN)
