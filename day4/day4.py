#!/usr/bin/python3
import sys

debug = False

file = sys.argv[1]
f = open(file).readlines()
puzzleArr = []

for line in f:
    puzzleArr.append(line.rstrip())


# How do we do this in a clever way?

def findChar (c, arr):
    known_pos = [] 
    row = 0
    col = 0
    for line in arr:
        col = 0
        for char in line:
            if char == c:
                known_pos.append([row, col])
            col += 1
        row +=1 
    return known_pos   

def searchXmas (arrX, arrM, arrA, arrS, x_dir, y_dir):
    found_full = []
    for x in arrX:
        row = x[0]
        col = x[1]
        found = []
        # print("Checking: ", x)
        for arr in arrM, arrA, arrS:
            if x_dir == 'left':
                row -= 1
            if x_dir == 'right':
                row += 1
            if y_dir == 'down':  # col increases as we go "down" as we look at it as humans
                col += 1
            if y_dir == 'up':  # col increases as we go "down" as we look at it as humans
                col -= 1
            if arr.count([row, col]):
                found.append([row, col])
            if len(found) == 3:   # Magic number, BUT XMAS is only ever four chars so we're good I think
                found_full.append(found)
   
    return found_full

def searchCrossmas (arrA, arrM, arrS):
    found_full = 0
    for a in arrA:
        topL_oob: False
        topR_oob = False
        botL_oob = False
        botR_oob = False
        found_m = 0
        found_s = 0
        row = a[0]
        col = a[1]
        # print("Checking: ", m)
        # We want to find "Exactly 2 M's and 2 S's"
        # check top left
        row -= 1
        col -= 1
        if arrM.count([row, col]):
            found_m += 1
            botR_oob = True
        # check top right
        row += 2
        if arrM.count([row, col]):
            found_m += 1
            botL_oob = True
        # check bottom right
        col += 2
        if (arrM.count([row, col]) and botR_oob == False):
            found_m += 1
        # check bottom left
        row -= 2
        if (arrM.count([row, col]) and botL_oob == False):
            found_m += 1
        
        # Only check S's if we have found exactly 2 M's
        if found_m == 2:
            # reset pos of 'A' before checking for S's
            row = a[0]
            col = a[1]
            # check top left
            row -= 1
            col -= 1
            if arrS.count([row, col]):
                found_s += 1
            # check top right
            row += 2
            if arrS.count([row, col]):
                found_s += 1
            # check bottom right
            col += 2
            if arrS.count([row, col]):
                found_s += 1
            # check bottom left
            row -= 2
            if arrS.count([row, col]):
                found_s += 1
            # print("m: ", found_m, "s: ", found_s)
            if found_m == 2 and found_s == 2:
                found_full += 1
                if debug:
                    print("Found X-MAS at A-Pos: ", a[0], a[1])
    return found_full


    


# known_x_pos = findChar('X', puzzleArr)
known_m_pos = findChar('M', puzzleArr)
known_a_pos = findChar('A', puzzleArr)
known_s_pos = findChar('S', puzzleArr)

# if debug:
#     # print('X: ', known_x_pos)
#     print('M: ', known_m_pos)
#     print('A: ', known_a_pos)
#     print('S: ', known_s_pos)

total = searchCrossmas(known_a_pos, known_m_pos, known_s_pos)

# total = searchXmas(known_x_pos,known_m_pos,known_a_pos,known_s_pos, 'right', '')
# total += searchXmas(known_x_pos,known_m_pos,known_a_pos,known_s_pos, 'left', '')
# total += searchXmas(known_x_pos,known_m_pos,known_a_pos,known_s_pos, '', 'down')
# total += searchXmas(known_x_pos,known_m_pos,known_a_pos,known_s_pos, '', 'up')
# total += searchXmas(known_x_pos,known_m_pos,known_a_pos,known_s_pos, 'left', 'up')
# total += searchXmas(known_x_pos,known_m_pos,known_a_pos,known_s_pos, 'left', 'down')
# total += searchXmas(known_x_pos,known_m_pos,known_a_pos,known_s_pos, 'right', 'up')
# total += searchXmas(known_x_pos,known_m_pos,known_a_pos,known_s_pos, 'right', 'down')

    # found = []
    # if known_m_pos.count([row - 1, col]):
    #     found.append([row - 1, col]) 
    #     if known_a_pos.count([row - 2, col]):
    #         found.append([row - 2, col]) 
    #         if known_s_pos.count([row - 3, col]):
    #             found.append([row - 3, col]) 
    #             found_left.append(found)
    
print("Total: ", total)

# print("found_right: ", len(found_right))
# print("found_left: ", len(found_left))
# print("found_down: ", len(found_down))
# print("found_up: ", len(found_up))
# print("found_diag_up_left", len(found_diag_up_left))
# print("found_diag_down_left", len(found_diag_down_left))
# print("found_diag_up_right", len(found_diag_up_right))
# print("found_diag_down_right", len(found_diag_down_right))