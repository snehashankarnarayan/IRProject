#!/usr/bin/python

from collections import Counter
from sets import Set

class statMaster:
    def __init__(self):
        #Globals
        self.wordCount = 0
        self.pageCount = 0
        self.bookCount = 0
        self.pageText = ""

        #Per book sets
        self.bookWordSet = Set()
        
        #Length of all books
        self.bookLengthList = []
        self.pageLengthList = []

        #Unique length of all books and pages
        self.bookUniqueLengthList = []
        self.pageUniqueLengthList = []

        self.bookLength = 0
        self.bookUniqueLength = 0

        #Global hashtables/dictionaries
        self.globalWordHash = Counter()
        self.bookWordHash = Counter()
        self.pageWordHash = Counter()

        #Word Correlation hashes
        self.strongHash = Counter()
        self.strongWindowHash = Counter()
        self.strongAdjacentHash = Counter()

        self.powerfulHash = Counter()
        self.powerfulAdjacentHash = Counter()
        self.powerfulWindowHash = Counter()

        self.butterHash = Counter()
        self.butterAdjacentHash = Counter()
        self.butterWindowHash = Counter()

        self.saltHash = Counter()
        self.saltAdjacentHash = Counter()
        self.saltWindowHash = Counter()

        self.jamesHash = Counter()
        self.jamesPrecedingHash = Counter()
        self.jamesAdjacentHash = Counter()
        self.jamesWindowHash = Counter()

        self.washingtonHash = Counter()
        self.washingtonPrecedingHash = Counter()
        self.washingtonAdjacentHash = Counter()
        self.washingtonWindowHash = Counter()

        self.churchHash = Counter()
        self.churchPrecedingHash = Counter()
        self.churchAdjacentHash = Counter()
        self.churchWindowHash = Counter()
