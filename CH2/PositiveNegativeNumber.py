#!/usr/bin/env python
num = raw_input('Enter a number > ')
try:
    number = int(num)
    if number == 0 :
        print "number is zero"
    elif number == abs(number):
        print "number is a integer"
    else :
        print "number is negative number"
except Exception, e:
    print "you enter not a number"
