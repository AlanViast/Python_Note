#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import string

initials = string.letters + '_'
digital = string.digits

print "Welcome to the Identifier Checker v1.0"
print "Testees must be at least 2 chars long."

myInput = raw_input("Identifier to test > ")

if len(myInput) > 1 :

  if myInput[0] not in initials :
    print '''
invalid: first symbol must be alphabetic
'''
  else :
    extChar = initials + digital
    for otherChar in myInput[1:] :
      if otherChar not in extChar :
        print "invalid: remaining symbols must be alphanumeric"
        break
    else :
      print "Okay as an identifier!"










