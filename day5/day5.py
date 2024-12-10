#!/usr/bin/python3

import sys
file = sys.argv[1]

f = open(file).readlines()
rules = [] # Tuples (assuming rules are only ever 2 ints) stored as Ints
updates = [] # List of lists stored as Ints

for line in f:
    if '|' in line:
        a, b = line.rstrip().split('|')
        rules.append((int(a), int(b)))
    elif ',' in line:
        nums = line.rstrip().split(',')
        l1 = []
        for num in nums:
            l1.append(int(num))
        updates.append(l1)

print("Rules: ", rules)
print("Updates: ", updates)

# We want to know which of the "Pages" match the rules

GoodUpdates = []

def is_a_first (a, b, numList):
    target = b
    found_a = False
    found_target = False
    for num in numList:
        # if we get to 'a' first, we can return True
        if found_a == True and found_target == False:
            return True
        # if get to target first this is BAD and we can break out
        elif found_target == True and found_a == False:
            return False
        if num == a:
            found_a = True
        elif num == target:
            found_target = True
    return True

def is_b_first (a, b, numList):
    target = a
    found_b = False
    found_target = False
    for num in numList:
        if num == b:
            found_b = True
        elif num == target:
            found_target = True
        # if we get to 'a' first, we need to keep checking
        if found_b == True:
            continue
        # if get to target first this is BAD and we can break out
        elif found_target == True and found_b == False:
            return True

    return True

# Loop through page number lists
for update in updates:
    updateValid = True
    # within each list loop through num
    for pageNum in update: 
        if updateValid == False:
            break
        # Check in rules for our num
        for rule in rules:
            a, b = rule
            # check each num against available rules
            # if num in rule
            # check if num is on LHS or RHS of tuple
            # check if rule is valid
            # Checking for LHS of tuple
            if pageNum == a: # LHS of tuple
                # print("Checking", rule, "LHS")
                if (is_a_first(a, b, update) == False):
                    updateValid = False
            elif pageNum == b:  # RHS of tuple
                if (is_b_first(a,b, update) == False):
                    updateValid = False
                
    if updateValid == False:
        print("Update Bad: ", update)
    else:
        print("Update Good: ", update)
        GoodUpdates.append(update)

part1Total = 0
for update in GoodUpdates:
    part1Total += update[int((len(update) + 1) / 2) - 1]

print("Part1 Total: ", part1Total)

# And then know the "middle" page to produce our total