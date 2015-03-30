#!/usr/bin/env python

'EditTextFile.py -- user can edit text file'

import curses
import time
import os


def readFile() :
    """ read text file function """
    # get filename
    fName = raw_input("Enter a file name > ")
    print

    fileContent = ""

    if not os.path.exists(fName) :
        print "File not found"
    else :
        try:
            fObj = open(fName)
        except IOError, e:
            print " *** file open error ***", e
        else :
            #display contents to the screen
            for eachLine in fObj :
                fileContent += eachLine
            fObj.close()
    return fileContent



def editText(text) :
    moveTuple = (curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN)

    # Init curses stdscr
    stdscr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(1)
    # get max X point and max Y point
    # scroll ok
    stdscr.scrollok(True)
    y = x = 0
    try:
        stdscr.addstr(0,0,text)
        stdscr.idcok(True)
        stdscr.idlok(1)
        maxY, maxX = stdscr.getmaxyx()
        # stdscr.scroll(1) #scroll screen
        stdscr.move(0, 20)
        stdscr.refresh()
        key = 'X'
        while True :
            y, x = stdscr.getyx()
            if key == ord('.') :
                break
            elif key == curses.KEY_BACKSPACE :
                if x != 0 :
                    stdscr.delch(y, x - 1)
                elif y != 0 :
                    stdscr.delch( y - 1 , maxX - 1)
                else :
                    curses.beep()
            elif key in moveTuple :
                moveCursor(key, stdscr)
            else :
                stdscr.addch(key)
            key = stdscr.getch()
            stdscr.refresh()
    finally:
        curses.nocbreak()
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()


def moveCursor(key, stdscr) :
    maxY, maxX = stdscr.getmaxyx()
    y, x = stdscr.getyx()
    if key == curses.KEY_LEFT :
        if x != 0 :
            x -= 1
        elif y != 0 :
            y -= 1
            x = maxX -1
    elif key == curses.KEY_RIGHT :
        if x != maxX - 1 :
            x += 1
        elif y != maxY -1 :
            y += 1
            x = 0
    elif key == curses.KEY_UP :
        if y != 0 :
            y -= 1
    elif key == curses.KEY_DOWN :
        if y != maxY - 1 :
            y += 1
    stdscr.move(y, x)



if __name__ == '__main__' :
    text = readFile()
    editText(text)






