#!/usr/bin/python

from collections import Counter
from sets import Set

class statMaster:

    #Globals
    wordCount = 0
    pageCount = 0
    bookCount = 0
    pageText = ""

    #Length of all books
    bookLengthList = []
    pageLengthList = []

    #Unique length of all books and pages
    bookUniqueLengthList = []
    pageUniqueLengthList = []

    bookLength = 0
    bookUniqueLength = 0

    #Global hashtables/dictionaries
    globalWordHash = Counter()
    bookWordHash = Counter()
    pageWordHash = Counter()

    #Word Correlation hashes
    strongHash = Counter()
    strongWindowHash = Counter()
    strongAdjacentHash = Counter()

    powerfulHash = Counter()
    powerfulAdjacentHash = Counter()
    powerfulWindowHash = Counter()

    butterHash = Counter()
    butterBookHash = Counter()
    butterWindowHash = Counter()

    saltHash = Counter()
    saltAdjacentHash = Counter()
    saltWindowHash = Counter()

    jamesHash = Counter()
    jamesAdjacentHash = Counter()
    jamesWindowHash = Counter()

    washingtonHash = Counter()
    washingtonAdjacentHash = Counter()
    washingtonWindowHash = Counter()

    churchHash = Counter()
    churchAdjacentHash = Counter()
    churchWindowHash = Counter()


    #Per book sets
    bookWordSet = Set()


