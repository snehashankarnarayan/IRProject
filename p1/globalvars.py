#!/usr/bin/python

from collections import Counter
from sets import Set

class globalvars:
    #Constants
    tinyDirName = "/phoenix/ir_code/data/books-tiny/"
    mediumDirName = "/phoenix/ir_code/data/books-medium/"
    smallDirName = "/phoenix/ir_code/data/books-small/"
    bigDirName = "/phoenix/ir_code/data/books-big/"

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

    #Per book sets
    bookWordSet = Set()

stats = globalvars()
