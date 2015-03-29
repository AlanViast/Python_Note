#!/usr/bin/env python
'readTextFile.py -- read and diaply text file'


import os

# get filename
fName = raw_input("Enter a file name > ")
print

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
            print eachLine.strip(),
        fObj.close()
