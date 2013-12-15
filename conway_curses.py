#!/usr/bin/env python

import curses
import time
import sys

from conway import Conway

def main():
    if len(sys.argv) > 1:
        tick_count = int(sys.argv[1])
    else:
        tick_count = 100

    # Initialize ncurses and get the board dimensions from the screen limits
    scr = curses.initscr()
    (x,y) = scr.getmaxyx()
    dim = min(x, y)

    # Use the lower bound to set the dimensions
    conway = Conway(bounds=(0,dim))

    # glider
    #initial_cells = [(1,0), (2,1), (0,2), (1,2), (2,2)]

    # blinker
    #initial_cells = [(1,0), (1,1), (1,2)]

    # random
    initial_cells = [(1,0), (2,1), (0,2), (1,2), (2,2), (5,5), (5,6), (5,7), (4,3), (4,2), (4,1), (3,4), (3,3), (5,2), (7,1), (7,3)]

    # Turn on the initialized cells
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

    scr.getch()
    curses.endwin()

if __name__ == '__main__':
    main()

