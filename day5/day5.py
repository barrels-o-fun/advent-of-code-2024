#!/usr/bin/python3

import sys
import time
file = sys.argv[1]

f = open(file).readlines()
rules = [] # Tuples (assuming rules are only ever 2 ints) stored as Ints
updates = [] # List of lists stored as Ints
GoodUpdates = [] # List of Good Updates (added to as we find them)
BadUpdates = []

# Read in rules and updates separately
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

# I feel like  this could be clearer, feels a bit messy...
# Would also be nice to have a single "is_x_first" function...
def is_b_first (a, b, numList):
    target = a
    found_b = False
    found_target = False
    for num in numList:
        if num == b:
            found_b = True
        elif num == target:
            found_target = True
        # if we get to 'b' first, we need to keep checking
        if found_b == True:
            continue
        # if get to target first this is BAD and we can break out
        elif found_target == True and found_b == False:
            return True

    return True

# Loop through page number lists

def processUpdates(updates, fixupdates = False):
    GoodUpdates = []
    BadUpdates = []
    for updateIndex, update in enumerate(updates):
        # print("Checking update:",  update)
        updateValid = True
        updateInvalidLHS = False
        updateInvalidRHS = True
        # within each list loop through num
        for index, pageNum in enumerate(update): 
            if updateValid == False:
                break
            # Check in rules for our num
            for rule in rules:
                if updateValid == False:
                    break
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
                    if fixupdates == True:
                        if updateInvalidLHS:
                            # print("Update: ", update, "bad due to rule LHS: ", rule, "index: ", index)
                            # switch indexes
                            lhs = update[index]
                            rhs = update[index + 1]
                            newUpdate = update.copy()
                            newUpdate[index] = rhs
                            newUpdate[index + 1] = lhs
                            # print("New proposed update: ", newUpdate)
                            updates[updateIndex] = newUpdate
                            updateValid = False
                        elif updateInvalidRHS:
                            # print("Update: ", update, "bad due to rule RHS: ", rule, "index: ", index)
                            # switch indexes
                            rhs = update[index]
                            lhs = update[index - 1]
                            newUpdate = update.copy()
                            newUpdate[index] = lhs
                            newUpdate[index - 1] = rhs
                            # print("New proposed update: ", newUpdate)
                            updates[updateIndex] = newUpdate
        if updateValid == False:
            # print("Update Bad: ", update)
            BadUpdates.append(updates[updateIndex])
        else:
            # print("Update Good: ", update)
            GoodUpdates.append(updates[updateIndex])

    return GoodUpdates, BadUpdates

part1Total = 0
part2Total = 0

GoodUpdates, BadUpdates = processUpdates(updates)
print("BadUpdates: ", BadUpdates)

finalFixedUpdates = []
unFixedUpdates = BadUpdates
while (len(unFixedUpdates) > 0):
    fixedUpdates, unFixedUpdates = processUpdates(unFixedUpdates, fixupdates=True)
    for fixed in fixedUpdates:
        finalFixedUpdates.append(fixed)
    # print("fixedUpdates: ", fixedUpdates)
    print("unFixedUpdates: ", len(unFixedUpdates))
    # time.sleep(1)

# for update in BadUpdates:
#     print("Still wrong: ", update)

for update in GoodUpdates:
    # Check the "middle" page to produce our total
    # length + 1 gives "human" length of list, div 2, then -1 to go back to index
    part1Total += update[int((len(update) + 1) / 2) - 1]

for update in finalFixedUpdates:
    part2Total += update[int((len(update) + 1) / 2) - 1]


print("Part 1 Total: ", part1Total)
print("Part 2 Total: ", part2Total)

