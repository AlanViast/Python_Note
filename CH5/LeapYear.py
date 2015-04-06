#!/usr/bin/env python
"Determine whether  a leap year"


def isLeapYear(years) :
    """ Determine whether  a leap year """
    if ( years % 100 != 0 and years % 4 == 0) or (years % 400 == 0) :
        return True
    else :
        return False

if __name__ == '__main__' :
    yearsStr = raw_input("Enter a years > ")
    years = int(yearsStr)
    flag = isLeapYear(years)
    if flag :
        print "%s is leap year" %years
    else :
        print "%s not is leap year" %years
