#!/usr/bin/python3
import tkinter as tk
from random import random

import sys
import time

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


root = tk.Tk()
# board_frame = tk.Frame(root, width=800, height=600)
# board_frame.pack()

i = 0
while True:
    board_frame = tk.Frame(root, width=400, height=400)
    board_frame.pack()
    i += 1
    time.sleep(1)
    grid = build_empty_grid()    
    # field = tk.Canvas(root, width=220,height=220)

    # field.pack()
    update_board(grid, i)
    root.update()
    time.sleep(1)

tk.mainloop()
    
