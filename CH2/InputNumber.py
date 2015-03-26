#!/usr/bin/env python

tempStr = raw_input("Enter a number > ")
try:
    number = int(tempStr)
    print "you enter a number is > %d" %(number)
except Exception, e:
    print "you enter not a number"
