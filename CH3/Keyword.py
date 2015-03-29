#!/usr/bin/env python

import keyword

keywordStr = raw_input("Enter a string > ")

if keyword.iskeyword(keywordStr) :
    print "`%s` is a keyword" %(keywordStr)
else :
    print "`%s` not a keyword" %(keywordStr)
