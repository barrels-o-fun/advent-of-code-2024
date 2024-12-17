#!/usr/bin/python3
import sys

debug = False

file = sys.argv[1]
f = open(file, 'r')

safeTotal = 0
unSafeTotal = 0

def checkViolations(splitLine, violationLevel):
    # Set up loop vars
    increasing = None # boolean to track whether previous numbers are increasing/decreasing
    safeLevel = 0
    cur = int(splitLine[0]) # set first instance as cur, then loop over [1:]
    for num in splitLine[1:]:
        safeLevelChange = False 
        if debug:
            print('safeLevel: %d' % safeLevel)
        new = int(num)
        if debug:
            print("Comparing %d to %d, increasing: %s" % (cur, new, increasing))
        if (abs(new - cur) > 3 or abs(new - cur) == 0):
            safeLevel += 1
            safeLevelChange = True
        if ((new - cur) > 0):
            if (increasing == False):
                safeLevel += 1
                safeLevelChange = True
            else:
                increasing = True
        if ((new - cur) < 0):
            if (increasing == True):
                safeLevel += 1
                safeLevelChange = True
            else:
                increasing = False
        if (safeLevelChange == False): # If safe level changed, keep last cur
            cur = new
    if (safeLevel > violationLevel):
        if debug:
            print("Declaring %s unsafe\n" % line.rstrip())
        return 1
    else:
        if debug:
            print("Declaring %s Safe\n" % line.rstrip())
        return 0



for line in f.readlines():
    if debug:
        print("Analyzing %s" % line)
    splitLine = (line.split(' '))
    if (checkViolations(splitLine, 1) == 0):
        if debug:
            print("Safe on FIRST pass")
        safeTotal += 1
    else:
        safe = False
        for i in range(0,(len(splitLine) - 1)):
            checkLine = splitLine.copy()
            checkLine.pop(i)
            if debug:
               print("checkline: ", checkLine)
            if(checkViolations(checkLine, 0) == 0):
                if debug:
                   print("Safe on pass: %d" % i)
                safe = True
                break
        if (safe == False):
            unSafeTotal +=1
            if debug: 
               print("Declared UnSafe")
            print("report: ", checkLine)
        else:
            safeTotal += 1

print("Safe: %d, Unsafe: %d" % (safeTotal, unSafeTotal))