#!/usr/bin/python

from statMaster import statMaster

myname = "snehas"

def getIndexOfTuple(tList, wordindex, value):
    for pos, item in enumerate(tList):
        if item[wordindex] == value:
            return pos

def generate_output(datasize, stats):
    outputFileName = "snehas_" + datasize + ".txt"
    fp = open(outputFileName, "w")
    
    #Output lines
    lines = []

    #Basic things
    line = myname + " " + datasize + " " + "N " + str(stats.bookCount) + " " + str(stats.pageCount) + "\n"
    lines.append(line)

    line = myname + " " + datasize + " " + "TO " + str(stats.wordCount) + "\n"
    lines.append(line)

    line = myname + " " + datasize + " " + "TU " + str(len(stats.bookWordSet)) + "\n"
    lines.append(line)
    
    #The top 50 things
    sortedList = stats.globalWordHash.most_common()

    for i in range(0, 50):
        item = sortedList[i]
        word = item[0]
        tokenPF = stats.pageWordHash[word]
        tokenBF = stats.bookWordHash[word]
        tokenTF = stats.globalWordHash[word]
        tokenP = round(float(tokenTF)/stats.wordCount, 8)
        tokenPR = tokenP * (i + 1)
        
        line = myname + " " + datasize + " " + str(i+1) + " " + word + " " + str(tokenBF) + " " + str(tokenPF) + " " + str(tokenTF) + " " + str(tokenP) + " " + str(tokenPR) + "\n"
        lines.append(line)
        
    
    #Dealing with the special words
    specialList = ["strong", "powerful", "butter", "salt", "james", "washington", "church"]
    for spl in specialList:
        rank = getIndexOfTuple(sortedList, 0, spl)
        tokenPF = stats.pageWordHash[spl]
        tokenBF = stats.bookWordHash[word]
        tokenTF = stats.globalWordHash[word]
        tokenP = round(float(tokenTF)/stats.wordCount, 8)
        tokenPR = tokenP * (rank + 1)
        
        line = myname + " " + datasize + " " + str(rank+1) + " " + spl + " " + str(tokenBF) + " " + str(tokenPF) + " " + str(tokenTF) + " " + str(tokenP) + " " + str(tokenPR) + "\n"
        lines.append(line)
        
    #Page Co-occurence stuff - powerful
    pageList = stats.powerfulHash.most_common(5)
    windowList = stats.powerfulWindowHash.most_common(5)
    adjacentList = stats.powerfulAdjacentHash.most_common(5)
    
    for i in range(0, len(adjacentList)):
        page = pageList[i][0]
        window = windowList[i][0]
        adjacent = adjacentList[i][0]
        line = myname + " " + datasize + " powerful " + page + " " + window + " " + adjacent + "\n"
        lines.append(line)

    #Page Co-occurence stuff - strong
    pageList = stats.strongHash.most_common(5)
    windowList = stats.strongWindowHash.most_common(5)
    adjacentList = stats.strongAdjacentHash.most_common(5)
    
    for i in range(0, len(adjacentList)):
        page = pageList[i][0]
        window = windowList[i][0]
        adjacent = adjacentList[i][0]
        line = myname + " " + datasize + " strong " + page + " " + window + " " + adjacent + "\n"
        lines.append(line)

    #Page Co-occurence stuff - butter
    pageList = stats.butterHash.most_common(5)
    windowList = stats.butterWindowHash.most_common(5)
    adjacentList = stats.butterAdjacentHash.most_common(5)
    
    for i in range(0, len(adjacentList)):
        page = pageList[i][0]
        window = windowList[i][0]
        adjacent = adjacentList[i][0]
        line = myname + " " + datasize + " butter " + page + " " + window + " " + adjacent + "\n"
        lines.append(line)

    #Page Co-occurence stuff - salt
    pageList = stats.saltHash.most_common(5)
    windowList = stats.saltWindowHash.most_common(5)
    adjacentList = stats.saltAdjacentHash.most_common(5)
    
    for i in range(0, len(adjacentList)):
        page = pageList[i][0]
        window = windowList[i][0]
        adjacent = adjacentList[i][0]
        line = myname + " " + datasize + " salt " + page + " " + window + " " + adjacent + "\n"
        lines.append(line)

    #Page Co-occurence stuff - washington
    pageList = stats.washingtonHash.most_common(5)
    windowList = stats.washingtonWindowHash.most_common(5)
    adjacentList = stats.washingtonAdjacentHash.most_common(5)
    
    for i in range(0, len(adjacentList)):
        page = pageList[i][0]
        window = windowList[i][0]
        adjacent = adjacentList[i][0]
        line = myname + " " + datasize + " washington " + page + " " + window + " " + adjacent + "\n"
        lines.append(line)

    #Page Co-occurence stuff - james
    pageList = stats.jamesHash.most_common(5)
    windowList = stats.jamesWindowHash.most_common(5)
    adjacentList = stats.jamesAdjacentHash.most_common(5)
    
    for i in range(0, len(adjacentList)):
        page = pageList[i][0]
        window = windowList[i][0]
        adjacent = adjacentList[i][0]
        line = myname + " " + datasize + " james " + page + " " + window + " " + adjacent + "\n"
        lines.append(line)

    
    #Page Co-occurence stuff - church
    pageList = stats.churchHash.most_common(5)
    windowList = stats.churchWindowHash.most_common(5)
    adjacentList = stats.churchAdjacentHash.most_common(5)
    
    for i in range(0, len(adjacentList)):
        page = pageList[i][0]
        window = windowList[i][0]
        adjacent = adjacentList[i][0]
        line = myname + " " + datasize + " church " + page + " " + window + " " + adjacent + "\n"
        lines.append(line)

    #Actually write to file
    fp.writelines(lines)
