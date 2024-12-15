#!/usr/bin/python3

import sys
import time

DEBUG = False

def add(a, b):
    if DEBUG:
        print("Adding:", a, b) 
    return a + b

def multiply(a, b):
    if DEBUG:
        print("Multiplying:", a, b)
    return a * b

def combine(a, b):
    a = str(a)
    b = str(b)
    result = a + b
    return result

def get_combinations_binary(numsList):
    combinations = []
    numsLen = len(numsList) - 1
    for num in range(0, (3 ** numsLen)):
        binNum = format(num, 'b')
        if len(binNum) < numsLen:
            binNum =  ('0' * (numsLen - len(binNum))) + binNum
        combinations.append(binNum)
    
    if DEBUG:
        print("Combinations:", combinations)
    return combinations
        
def calculate_from_combo(numsList, combinations):
    firstNum = int(numsList.pop(0))
    for combo in combinations:
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
            if DEBUG:
                print("Found one!", res)
            return 0, res
    # return 1 if we haven't found a good combo
    return 1, 0

def createCombinedNumberOptions(l):
    results = []
    results.append(l)
    for i in range(0, (len(l) - 1)):
        lTemp = l.copy()
        lTemp.pop(i)
        lTemp.pop(i)
        num1 = l[i]
        num2 = l[i + 1]
        result = combine(num1, num2)
        lTemp.insert(i, result)
        results.append(lTemp)
    return results



##############
# Start here #
##############

input_file = sys.argv[1]
good_ones = 0
part1_total = 0

input_data = open(input_file).readlines()

for line in input_data:
    total = 0
    res, nums = line.split(": ")
    res = int(res)
    numsList = nums.rstrip().split(' ')
    if DEBUG:
        print(len(numsList), repr(numsList))
    all_combos = createCombinedNumberOptions(numsList)
    for combo in all_combos:
        combo_total = 0
        # print("Checking combo: ", combo)
        combinations = get_combinations_binary(combo)
        result, combo_total = calculate_from_combo(combo, combinations)
        if combo_total != 0:
            good_ones += 1
            part1_total += combo_total

print("Total rows: ", len(input_data))
print("Good:", good_ones)
print("Part1:", part1_total)


# if len = 2, combos are 2**2
# + +  00
# + *  01 
# * +  10
# * *  11


# if len = 3, combos are 3**2
# + + + 0 0 0
# + + * 0 0 1
# + * +
# + * *
# * + +
# * + *
# * * +
# * * *

 # len 4 = 16 combinations   
