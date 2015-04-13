#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def remainder() :
  evenList = [x for x in range(1, 21) if x % 2 == 0 ]
  return evenList

def oddNumber() :
  oddList = [ x for x in range(1, 21) if x % 2 != 0]
  return oddList

def divisible(num1 , num2) :
  if isNumber(num1) and isNumber(num2):
    return num1 % num2 == 0


def isNumber(obj) :
  return isinstance(obj, (int, long))

if __name__ == '__main__':
  print remainder()
  print oddNumber()

  num1 = int(raw_input("Enter num1 > "))
  num2 = int(raw_input("Enter num2 > "))

  print divisible(num1, num2)
