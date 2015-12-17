#!/usr/bin/env python

import curses
import time
import sys
import os

from conway import Conway

def read_initial_state_file(initial_file):
    with open(initial_file) as f:
        grid = f.readlines()

    initial_cells = []
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char.strip() == '*':
                initial_cells.append((x, y))

    return initial_cells

def main():
    if len(sys.argv) > 1:
        tick_count = int(sys.argv[1])
    else:
        tick_count = 20

    # Initialize ncurses and get the board dimensions from the screen limits
    scr = curses.initscr()
    (x,y) = scr.getmaxyx()
    dim = min(x, y)

    # Use the lower bound to set the dimensions
    conway = Conway(bounds=(0,dim))

    # Turn on the initialized cells
    initial_cells = read_initial_state_file('initial_state.txt')
    for cell in initial_cells:
            conway.set_initial_state_on_board(cell, True)

    scr.keypad(0)
    curses.noecho()
    curses.curs_set(0)

    # Draw the live cells on the screen and update tick
    for i in range(tick_count):
        scr.clear()
        for position in conway.get_alive_positions():
            # Draw as an asterisk
            scr.addstr(position[0],position[1],'*')
            scr.refresh()

        # Slow down if necessary
        time.sleep(.5)

        # Update each cells future state
        conway.update_each_cells_state()

        # Update the board all at once
        conway.update_board()
    
    # No ticks left, all done
    cleanup()

def cleanup():
    curses.endwin()
    os.system('stty sane')
    os.system('reset')
    sys.exit(0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
