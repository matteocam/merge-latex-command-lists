#!/usr/bin/python

from sys import argv

def readAllLinesFromFile(fn):
    f = open(fn)
    return f.readlines()

def getUniqLines(lines):
    s = set()

    result = []
    wasLastLineBlank = False

    for l in lines:
        # Deal with "empty lines" differently to avoid repetition
        if l == "\n":
                if wasLastLineBlank:
                    continue # no need to repeat this
                result.append(l)
                wasLastLineBlank = True
                continue

        # If we get here, it means l is not blank
        
        if l not in s:
            # we output it 
            result.append(l)
            # we add the line to set 
            s.add(l)
            wasLastLineBlank = False

    return result
            

if __name__ == '__main__':
    if len(argv) < 2:
        print "Usage: merge.py input1 input2..."

    filenames = argv[1:]

    allLinesUnflat = [readAllLinesFromFile(fn) for fn in filenames]
    allLines = [l for lines in allLinesUnflat for l in lines ]

    #print ''.join(allLines)

    uniqLines = getUniqLines(allLines)

    print ''.join(uniqLines)
    
        
