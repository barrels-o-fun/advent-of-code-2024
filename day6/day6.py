# Set up basic UI to display grid

#!/usr/bin/python3
import tkinter as tk

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


file = sys.argv[1]

f = open(file).readlines()

grid = []
grid2 = []
visited_tiles = 0

for i, line in enumerate(f):
    mainArr = []
    secondArr = []
    for char in line.rstrip():
        mainArr.append(char)
        secondArr.append(' ')
    grid.append(mainArr)
    grid2.append(secondArr)

line_length = len(line)
array_height = len(grid)


# for i in range(1, 10):
#     internalArr = []
#     for j in range(1, 10):
#         internalArr.append('X')
#     grid.append(internalArr)


tk_grid_col_width = 15
tk_grid_row_height = 15
X_OFFSET = 20

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

root = tk.Tk()
board_frame = tk.Frame(root, width=600, height=400)
board_frame.pack()

# find player char
def find_guard(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == '^':
                return i, j

def move_guard(grid, grid2, guard_pos, guard_char, visited_tiles):
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

    if grid2[y][x] != 'X':
        grid2[y][x] = 'X'
        visited_tiles += 1

    new_x = x + x_adj
    new_y = y + y_adj

    # check collision
    try:
       if grid[new_y][new_x] == '#':
           check = True
    except IndexError:
        print("Near OOB")
        return grid, grid2, (new_y, new_x), guard_char, visited_tiles
        

    if grid[new_y][new_x] == '#':
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
        grid[y][x] = '.'
        grid[new_y][new_x]  = guard_char
    
    return grid, grid2, (new_y, new_x), guard_char, visited_tiles

def print_grid(grid):
    for line in grid:
        print(line)


  

y, x = find_guard(grid)
guard_pos = (y, x)
guard_char = '^'

while True:
    # print("Guard found: ", x, y)
    # print_grid(grid)
    # update_grid(grid, 0)
    # update_grid(grid2, 256)
    grid, grid2, guard_pos, guard_char, visited_tiles = move_guard(grid, grid2, guard_pos, guard_char, visited_tiles)
    guard_posy, guard_posx = guard_pos
    if guard_posx < 0 or guard_posx > line_length or guard_posy < 0 or guard_posy > array_height - 1:
        break
    # time.sleep(1)
    print("Guard_pos: ", guard_char, guard_pos)
    # root.update()

print("Tiles: ", visited_tiles)

    
# tk.mainloop()
