#!/usr/bin/env python



def displayNumType(num) :
    """ display number type """
    print num, "is",

    if isinstance(num, (int, long, float, complex)) :
        print "a number of type: ", type(num).__name__
    else :
        print "not a number at all!!!"






if __name__ == '__main__':
    displayNumType(-99)
    displayNumType(9999999999999999999999999999999L)
    displayNumType(98.7)
    displayNumType(-5.2+1.9j)
    displayNumType('xxxx')




