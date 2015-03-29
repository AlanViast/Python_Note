#!/usr/bin/env python
'EditTextFile.py -- user can edit text file'

import curses
import time
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(1)

try:

    # Print Hello World along the top
    stdscr.addstr(0,0,"Hello World")


    stdscr.refresh()
    key = 'X'
    while key != ord('.'):
        key = stdscr.getch()
        stdscr.addch(key)
        stdscr.refresh()
finally:
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()










