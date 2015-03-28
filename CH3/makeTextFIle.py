#!/usr/bin/env python

'makeTextFile.py --create text file'

import os
ls = os.linesep
fName = ''
#Get FileName
while True :
    fName = raw_input("Enter a file name > ")
    if os.path.exists(fName) :
        print "Error : '%s' already exists" %(fName)
    else :
        break

# Get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit)"

# Loop until user terimates input
while True :
    entry = raw_input("> ")
    if entry == "." :
        break
    else :
        all.append(entry)

# Write lines to file with proper line-ending
fObj = open(fName, "w")
fObj.writelines(['%s%s' %(x, ls) for x in all])
fObj.close()
print "Done!"
