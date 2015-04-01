#!/usr/bin/env python

'TextFile.py --create text file or read text file'

import os
ls = os.linesep
fName = ''


def makeTextFile():
    "create a text file"
    # Get FileName
    while True:
        fName = raw_input("Enter a file name > ")
        if os.path.exists(fName):
            print "Error : '%s' already exists" % (fName)
        else:
            break
    # Get file content (text) lines
    all = []
    print "\nEnter lines ('.' by itself to quit)"

    # Loop until user terimates input
    index = 1
    while True:
        tempStr = "%d > " % (index)
        entry = raw_input(tempStr)
        if entry == ".":
            break
        else:
            all.append(entry)
        index += 1

    # Write lines to file with proper line-ending
    try:
        fObj = open(fName, "w")
    except IOError, e:
        print " *** file open error ***", e
    else:
        fObj.writelines(['%s%s' % (x, ls) for x in all])
        fObj.close()


def readTextFile():
    "read text file"
    # get filename
    fName = raw_input("Enter a file name > ")
    print "\n"

    if not os.path.exists(fName):
        print "File not found"
    else:
        try:
            fObj = open(fName)
        except IOError, e:
            print " *** file open error ***", e
        else:
            # display contents to the screen
            for eachLine in fObj:
                print eachLine.strip()
            fObj.close()


def main():
    "main function"
    menu = """
(R)ead File
(M)ake File
e(X)it
Enter a choice > """
    while True:
        choice = raw_input(menu)
        if "X" == choice:
            break
        elif "R" == choice:
            readTextFile()
        elif "M" == choice:
            makeTextFile()

if __name__ == '__main__':
    main()
    print "Done!"
