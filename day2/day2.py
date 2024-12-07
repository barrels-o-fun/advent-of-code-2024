#!/usr/bin/python3
import sys

debug = True

file = sys.argv[1]
# sep = '   '
f = open(file, 'r')

safeTotal = 0
unSafeTotal = 0

for line in f.readlines():
    # Need to catch cases where removing the first number would result in a positive result
    unSafe = False
    if debug:
        print("Analyzing %s" % line)
    splitLine = (line.split(' '))
    increasing = None
    increaseFlips = 0
    cur = int(splitLine[0])
    safeLevel = 0
    for num in splitLine[1:]:
        safeLevelChange = False
        if debug:
            print('safeLevel: %d' % safeLevel)
        if(safeLevel > 1):
            break
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
        if (safeLevelChange == False):
            cur = new
    if (safeLevel > 1):
        if debug:
            print("Declaring %s unsafe" % line.rstrip())
        unSafeTotal += 1
    else:
        safeTotal += 1


print("Safe: %d, Unsafe: %d" % (safeTotal, unSafeTotal))