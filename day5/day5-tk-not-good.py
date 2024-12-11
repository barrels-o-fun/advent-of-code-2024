#!/usr/bin/python3

import tkinter as tk
from random import random

import sys
import time
# file = sys.argv[1]
file = 'sampleData.txt'

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

# print("Rules: ", rules)
# print("Updates: ", updates)

# We want to know which of the "Pages" match the rules
width = 2
blank = '     '

tk_grid_col_width = 75
tk_grid_row_height = 75
X_OFFSET = 128

def build_empty_grid():
    grid = [[blank,] * width,
           [blank,] * width
           ]
    return grid

def update_board(grid, value):
    bg_color = 'white'
    text_color = 'black'
    y_offset = 0
    for row in grid:
        for cnt, piece in enumerate(row):
            if (False):
                continue
            else:
                icon = value
            w = tk.Label(root, text= icon, bg = bg_color, fg = text_color)
            w.place(x = 0 + (cnt * tk_grid_col_width ) + X_OFFSET, y = 0 + y_offset, width = tk_grid_col_width, height = tk_grid_row_height)
            if bg_color == 'white':
                bg_color = 'black'
                text_color = 'white'
            else:
                bg_color = 'white'
                text_color = 'black'
        if bg_color == 'white':
            bg_color = 'black'
            text_color = 'white'
        else:
            bg_color = 'white'
            text_color = 'black'    
        y_offset += tk_grid_row_height



# Main starts here




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


#Main starts here



root = tk.Tk()

grid = build_empty_grid()    

# field = tk.Canvas(root, width=220,height=220)
board_frame = tk.Frame(root, width=800, height=600)
board_frame.pack()
# field.pack()
update_board(grid, 0)
part1Total = 0
part2Total = 0

finish = False
fixingUpdates = False
finalFixedUpdates = []

def run_game (part1Total, part2Total, updates, unFixedUpdates, fixingUpdates):
   

        if(fixingUpdates == False):
            GoodUpdates, BadUpdates = processUpdates(updates)
            print("BadUpdates: ", BadUpdates)

            unFixedUpdates = BadUpdates
            fixingUpdates = True
            update_board(grid, len(unFixedUpdates))
            return False, unFixedUpdates
    

        else:
            if (len(unFixedUpdates) > 0):
                fixedUpdates, unFixedUpdates = processUpdates(unFixedUpdates, fixupdates=True)
                for fixed in fixedUpdates:
                    finalFixedUpdates.append(fixed)
                print("unFixedUpdates: ", len(unFixedUpdates))
                update_board(grid, len(unFixedUpdates))
                # time.sleep(1)
            else:
                return False, unFixedUpdates

        # for update in BadUpdates:
        #     print("Still wrong: ", update)

        for update in GoodUpdates:
            # Check the "middle" page to produce our total
            # length + 1 gives "human" length of list, div 2, then -1 to go back to index
            part1Total += update[int((len(update) + 1) / 2) - 1]

        for update in finalFixedUpdates:
            part2Total += update[int((len(update) + 1) / 2) - 1]



unFixedUpdates = []
while (finish == False):
    print("Beginning")
    finish, unFixedUpdates = run_game(part1Total, part2Total, updates, unFixedUpdates, fixingUpdates)
    print("Here now")
    root.update()

tk.mainloop()
    
    # print("Part 1 Total: ", part1Total)
    # print("Part 2 Total: ", part2Total)

    


    # button = tk.Button(
    # master=root,
    # text="Click me!",
    # width=25,
    # height=5,
    # bg="blue",
    # fg="yellow",
    # command = lambda : build_empty_grid()
    # )
    # button.pack()
    # next_button = tk.Button(root, text="Next Iteration", command=lambda : run_and_canvas(board, field))
    # next_button.pack()
    # init_button = tk.Button(root, text="New Initialization", command=lambda : random_init(board, field))
    # init_button.pack()
    # tk.mainloop()