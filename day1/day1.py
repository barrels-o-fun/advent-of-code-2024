#!/usr/bin/python3

import sys
import pprint

file = sys.argv[1]
sep = '   '
f = open(file, 'r')

splits1 = []
splits2 = []

for line in f.readlines():
    splits1.append(line.split(sep)[0].rstrip())
    splits2.append(line.split(sep)[1].rstrip())

splits1.sort()
splits2.sort()

total = 0
for i in range(0, len(splits1)):
    total += abs(int(splits1[i]) - int(splits2[i]))

total2 = 0
for i in range(0, len(splits1)):
    total2 += (int(splits1[i]) * int(splits2.count(splits1[i])))


print("Part 1 Total: ", total)
print("Part 2 Total: ", total2)

