#!/usr/bin/python3
import sys

debug = False

file = sys.argv[1]
# sep = '   '
f = open(file, 'r')

safeTotal = 0
unSafeTotal = 0

for line in f.readlines():
    unSafe = False
    if debug:
        print("Analyzing %s" % line)
    splitLine = (line.split(' '))
    increasing = None
    cur = int(splitLine[0])
    for num in splitLine[1:]:
        new = int(num)
        if debug:
            print("Comparing %d to %d, increasing: %s" % (cur, new, increasing))
        if (abs(new - cur) > 3 or abs(new - cur) == 0):
            unSafe = True
            break
        if ((new - cur) > 0):
            if (increasing == False):
                unSafe = True
                break
            else:
                increasing = True
        if ((new - cur) < 0):
            if (increasing == True):
               unSafe = True
               break
            else:
                increasing = False
        cur = new
    if (unSafe):
        unSafeTotal += 1
    else:
        safeTotal += 1

print("Safe: %d, Unsafe: %d" % (safeTotal, unSafeTotal))