# Set up basic UI to display grid

#!/usr/bin/python3
import tkinter as tk

import os
import sys
import time

'''
[y][x]

   0123456789
[0]....#.....
[1].........#
[2]..........
[3]..#.......
[4].......#..
[5]..........
[6].#..^.....
[7]........#.
[8]#.........
[9]......#...
'''

test_grid = [
'....#.....\n',
'.........#\n',
'..........\n',
'..#.......\n',
'.......#..\n',
'..........\n',
'.#.O^.....\n',
'........#.\n',
'#.........\n',
'......#...\n'
]


def set_state(initialState):
    for line in initialState:
        mainArr = []
        secondArr = []
        thirdArr = []
        for char in line.rstrip():
            mainArr.append(char)
            secondArr.append(' ')
            thirdArr.append(' ')
        grid_start.append(mainArr)
        grid_record_walked.append(secondArr)
        grid_obstacles.append(thirdArr)
    return grid_start, grid_record_walked, grid_obstacles

def clear_grid(grid):
    for i, col in enumerate(grid):
        for j, row in enumerate(col):
            grid[j][i] = ' '
    return grid

def reset_grid_state(grid, initialState):
    grid = []
    for line in initialState:
        mainArr = []
        for char in line.rstrip():
            mainArr.append(char)
        grid.append(mainArr)
    return grid

def print_grid(grid):
    for line in grid:
        printMe = ''
        for char in line:
            printMe += char
        print(printMe)

# simple function to update grid on demand (b/w)
def update_grid(grid, offset_plus):
    bg_color = 'white'
    text_color = 'black'
    y_offset = 0
    for row in grid:
        for cnt, piece in enumerate(row):
            if (False):
                continue
            else:
                icon = piece
            w = tk.Label(root, text= icon, bg = bg_color, fg = text_color)
            w.place(x = 0 + (cnt * tk_grid_col_width ) + X_OFFSET + offset_plus, y = 0 + y_offset, width = tk_grid_col_width, height = tk_grid_row_height)
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

# find player char
def find_guard(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == '^':
                return i, j

def move_guard(grid, grid_record_walked, grid_obstacles, guard_pos, guard_char, visited_tiles, visit_plus_dir, populate_obstacles = False):
    # guard_chars = ['^', '>', 'V', '<']
    y, x = guard_pos
    x_adj = 0
    y_adj = 0
    # Check guard_char so we know direction
    if guard_char == '^':
        y_adj = -1
    elif guard_char == '>':
        x_adj = 1
    elif guard_char == 'V':
        y_adj = 1
    elif guard_char == '<':
        x_adj = -1

    if grid_record_walked[y][x] != 'X':
        grid_record_walked[y][x] = 'X'
        visited_tiles += 1

    new_x = x + x_adj
    new_y = y + y_adj

    # check collision
    try:
       if grid[new_y][new_x] == '#':
           grid_record_walked[new_y][new_x] = '#'
           grid_obstacles[new_y][new_x] = '#'
           check = True

    except IndexError:
        print("Near OOB: ", new_y, new_x)
        return 1, grid, grid_record_walked, grid_obstacles, (new_y, new_x), guard_char, visited_tiles, visit_plus_dir
        

    if grid[new_y][new_x] in ['#', 'O']:
        # print("Checking against: ", ((y,x), guard_char))
        # record pos + dir
        for check in visit_plus_dir:
                # print("Check: ", check)
                if check == ([(y, x), guard_char]):
                    # print("We've been here before")
                    # time.sleep(1)
                    return 2, grid, grid_record_walked, grid_obstacles, (new_y, new_x), guard_char, visited_tiles, visit_plus_dir
        visit_plus_dir.append([(y, x), guard_char])
        # rotate 90 deg
        if guard_char == '^':
            guard_char = '>'
        elif guard_char == '>':
            guard_char = 'V'
        elif guard_char == 'V':
            guard_char = '<'
        elif guard_char == '<':
            guard_char = '^'
        else:
            print("Shouldn't get here")
            exit
        # reset guard pos
        new_x = x
        new_y = y

        
    else:
        try:
            grid[y][x] = '.'
            grid[new_y][new_x]  = guard_char

            if populate_obstacles == True:
                if guard_char == '^':
                    grid_obstacles[new_y - 1][new_x] = 'O'
                elif guard_char == '>':
                    grid_obstacles[new_y][new_x + 1] = 'O'
                elif guard_char == 'V':
                    grid_obstacles[new_y + 1][new_x] = 'O'
                elif guard_char == '<':
                    grid_obstacles[new_y][new_x - 1] = 'O'
                else:
                    print("Shouldn't get here")
                    exit
        except IndexError:
            print("It's ok")
        
    
    return 0, grid, grid_record_walked, grid_obstacles, (new_y, new_x), guard_char, visited_tiles, visit_plus_dir

def run_game(grid_start, grid_record_walked, grid_obstacles, guard_pos, guard_char, visited_tiles, grid_count = 0, populate_obstacles = False):
    visit_plus_dir = []
    already_seen_this = False
    while (already_seen_this == False):
        # print("Guard found: ", guard_pos)
        # os.system('cls')
        # print("Grid count: ", grid_count)
        # print_grid(grid_record_walked)
        if populate_obstacles == False:
            result, grid_start, grid_record_walked, grid_obstacles, guard_pos, guard_char, visited_tiles, visit_plus_dir = move_guard(grid_start, grid_record_walked, grid_obstacles, guard_pos, guard_char, visited_tiles, visit_plus_dir, populate_obstacles = False)
        else:
            result, grid_start, grid_record_walked, grid_obstacles, guard_pos, guard_char, visited_tiles, visit_plus_dir = move_guard(grid_start, grid_record_walked, grid_obstacles, guard_pos, guard_char, visited_tiles, visit_plus_dir, populate_obstacles = True)
        guard_posy, guard_posx = guard_pos
        if guard_posx < 0 or guard_posx > line_length or guard_posy < 0 or guard_posy > array_height - 1:
            # print("Final guard_pos: ", guard_posy, guard_posx)
            # time.sleep(2)
            break
        # time.sleep(0.1)
        # print("Guard_pos: ", guard_char, guard_pos)
        # update_grid(grid, 0)
        # update_grid(grid_record_walked, 256)
        # root.update()
        if result == 1:
            # OOB
            return 1, grid_start, grid_obstacles
        elif result == 2:
            already_seen_this = True
            return 2, grid_start, grid_obstacles
        # print("Visited: ", visited_tiles, visit_plus_dir)
        # time.sleep(0.1)
    # print("Visited: ", visited_tiles, visit_plus_dir)
    return 0, grid_start, grid_obstacles

#
#  Main  starts here
#

file = sys.argv[1]

tk_grid_col_width = 15
tk_grid_row_height = 15
X_OFFSET = 20

root = tk.Tk()
board_frame = tk.Frame(root, width=600, height=400)
board_frame.pack()

# Summary
# Reset game start to start
# Add additional (O)bstacle
# Run Game
# Repeat

initialState = open(file).readlines()
# initialState = test_grid
print("InitalState: ", initialState)

grid_start = []
grid_record_walked = []
grid_obstacles = []
visited_tiles = 0

grid_start, grid_record_walked, grid_obstacles = set_state(initialState)

print_grid(grid_start)

array_height = len(grid_start)
line_length = len(grid_start[0])

guard_start_col, guard_start_row = find_guard(grid_start)
guard_pos = (guard_start_col, guard_start_row)
guard_char = '^'
bad_game = 0
good_game = 0
oob_game = 0

update_grid(grid_start, 0)
update_grid(grid_record_walked, 256)

result, grid_start, grid_obstacles = run_game(grid_start, grid_record_walked, grid_obstacles, guard_pos, guard_char, visited_tiles, populate_obstacles = True)

print("resetting)")
grid_start = reset_grid_state(grid_start, initialState)

print_grid(grid_start)

grid_count = 0

print_grid(grid_obstacles)

for i, col in enumerate(grid_obstacles):
    for j, row in enumerate(grid_obstacles):
        if grid_obstacles[j][i] == 'O':
            print("Obstacle found: ", j, i)

print("grids: ", grid_count)



for i, row in enumerate(grid_obstacles):
    for j, col in enumerate(row):
        result = 0
        # print("=== DEBUG - Grid pos:", i, j, "Char: ", grid_obstacles[i][j] )
        if grid_obstacles[j][i] == 'O':
            grid_count += 1
            # print("Checking against obstacle: ", i, j)
            grid = clear_grid(grid_record_walked)
            grid_start = reset_grid_state(grid_start, initialState)
            guard_pos = (guard_start_col, guard_start_row)
            guard_char = '^'
            grid_start[j][i] = 'O'
            # print("Checking next grid: ", grid_count, "Guard: ", guard_pos, guard_char)
            # print_grid(grid_start)
            # time.sleep(2)
            result, grid_start, _ = run_game(grid_start, grid_record_walked, grid_obstacles, guard_pos, guard_char, visited_tiles)
            if result == 0:
                bad_game += 1
            elif result == 1:
                oob_game += 1
            else:
                # print("== DEBUG game returned state: 2", "Grid pos:", j, i, "Char: ", grid_obstacles[j][i])
                # print_grid(grid_start)
                good_game += 1
        else:
            continue
    
    # print("Final Grid State:")
    # print_grid(grid_start)
    # time.sleep(1)        

print("Grid area : ", len(grid_start) * len(grid_start[0]))
print("Total Games: ", grid_count)
print("Good: ", good_game, "Bad: ", bad_game, "OOB: ", oob_game)

            
            


    
# tk.mainloop()
