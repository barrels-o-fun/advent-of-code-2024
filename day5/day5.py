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




# If LHS
#   loop through list of pageNums
#   check if we get to a or b first
#   if get to 'a' first this is GOOD and we can break out
#   if get to 'b' first this is BAD and we can break out
# Loop through pageNums 

GoodUpdates = []

# Loop through page number lists
for update in updates:
    updateValid = True
    # print("Checking update: ", update)
    # within each list loop through num
    for pageNum in update: 
        if updateValid == False:
            break
        # num = int(num)  # I thought I had these as Ints already but ok :-D, yup I was an idiot :D
        # Check in rules for our num
        for rule in rules:
            # check each num against available rules
            # print("Checking rule: ", rule)
            # print(rule)
            a, b = rule
            # print("a: ", repr(a))
            # if num in rule
            # check if num is on LHS or RHS of tuple
            # check if rule is valid
            # Checking for LHS of tuple
            if pageNum == a: # LHS of tuple
                # print("Checking", rule, "LHS")
                target = b
                found_a = False
                found_target = False
                # print("Found num", pageNum, "as 'A' in rule: ", rule)
                # loop through list of pageNums
                for num in update:
                    # print("Checking against: ", num)
                    # check if we get to a or b first
                    # if get to 'b' first this is BAD and we can break out
                    if found_target == True:
                        updateValid = False
                        # print("Rule Bad: ", update, "Due to rule: ", rule)
                        break
                    # if get to 'a' first this is GOOD and we can break out
                    elif found_a == True:
                        continue
                    if num == a:
                        found_a = True
                    elif num == target:
                        found_target = True

            elif pageNum == b:  # RHS of tuple
                # print("Checking", rule, "RHS")
                target = a
                found_b = False
                found_target = False
                # print("Found num", pageNum, "as 'A' in rule: ", rule)
                # loop through list of pageNums
                for num in update:
                    # print("Checking against: ", num)
                    # check if we get to a or b first
                    # if get to 'b' first this is BAD and we can break out
                    if found_target == True:
                        break
                    # if get to 'a' first this is GOOD and we can break out
                    elif found_target == True and found_b == False:
                        updateValid = False
                        # print("Rule Bad: ", update, "Due to rule: ", rule)
                        break
                    if num == b:
                        found_b = True
                    elif num == target:
                        found_target = True

                # print("Found num", pageNum, "as 'B' in rule: ", rule)
                
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