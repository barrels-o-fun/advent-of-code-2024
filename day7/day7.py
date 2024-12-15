#!/usr/bin/python3

import sys

DEBUG = False

input_file = sys.argv[1]
good_ones = 0
part1_total = 0


input_data = open(input_file).readlines()

def add(a, b):
    if DEBUG:
        print("Adding:", a, b) 
    return a + b

def multiply(a, b):
    if DEBUG:
        print("Multiplying:", a, b)
    return a * b

for line in input_data:
    total = 0
    res, nums = line.split(": ")
    res = int(res)
    numsList = nums.rstrip().split(' ')
    if DEBUG:
        print(len(numsList), repr(numsList))
    combinations = []
    numsLen = len(numsList) - 1
    for num in range(0, (2 ** numsLen)):
        binNum = format(num, 'b')
        if len(binNum) < numsLen:
            binNum =  ('0' * (numsLen - len(binNum))) + binNum
        combinations.append(binNum)
    
    if DEBUG:
        print("Combinations:", combinations)

    firstNum = int(numsList.pop(0))
    for i, combo in enumerate(combinations):
        # print("Checking combination:", combo)
        total = firstNum
        for j in range(0, len(numsList)):
            # print("numsList: ", numsList[j])
            if combo[j] == '0':
                total = add(total, int(numsList[j]))
                # print("total: ", total)
            elif combo[j] == '1':
                total = multiply(total, int(numsList[j]))
            else:
                print("How did we get here?")
        if DEBUG:
            print("Result", res, total)
        if total == res:
            print("Found one!", res)
            good_ones += 1
            part1_total += res
            break
    # check if '*' gives res

print("Good:", good_ones)
print("Part1:", part1_total)



# if len = 2, combos are
# + +  00
# + *  01 
# * +  10
# * *  11


# if len = 3, combos are:
# + + + 0 0 0
# + + * 0 0 1
# + * +
# + * *
# * + +
# * + *
# * * +
# * * *


 # len 4 = 16 combinations   
