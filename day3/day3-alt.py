#!/usr/bin/python3

import sys
import re

file = sys.argv[1]
f = open(file, 'r')

# s1 = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
total = 0
validre = 'mul\(\d+,\d+\)'

for line in f.readlines():
    print("=== New Line ===")
    # print("line %s" % line)
    splitLines = line.split("do()")
    validLines = []
    # validLines.append(splitLines[0])
    for line in splitLines:
        validLine = ''
        # print("Analyzing %s\n\n" % line)
        if ("don't()" in line):
            validLine = line.split("don't()")[0]
            # print("Appending %s \n\n" % validLine)
            validLines.append(validLine)
        else:
            # print("No don'ts found in this line %s" % line)
            validLines.append(line)


    for line in validLines:
        l1 = re.findall(validre, line)
        print(l1)
        print("Len %d" % len(l1))

        for i in l1:
            result = 0
            s1 = i
            multi = s1[s1.index('(')+ 1:s1.index(')')].split(',')
            result = int(multi[0]) * int(multi[1])
            total += result

print("Total %d" % total)
