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
index = 1
while True :
    tempStr = "%d > " %(index)
    entry = raw_input(tempStr)
    if entry == "." :
        break
    else :
        all.append(entry)
    index += 1

# Write lines to file with proper line-ending
try:
    fObj = open(fName, "w")
except IOError, e:
    print " *** file open error ***", e
else :
    fObj.writelines(['%s%s' %(x, ls) for x in all])
    fObj.close()

print "Done!"
