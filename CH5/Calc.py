#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def calc(equation) :
  if isinstance(equation, str) :
    operandList = equation.strip().split(" ")
    if 3 != len(operandList) :
      print "操作数不足三位不能进行运算"
    else :
      num1 = float(operandList[0])
      num2 = float(operandList[2])
      result = calculateDict[operandList[1]](num1, num2)
      print "%s = %d" %(equation, result)


def addition(num1, num2) :
  return num1 + num2

def subtraction(num1, num2) :
  return num1 - num2


def multiplication(num1, num2) :
  return num1 * num2

def division(num1, num2) :
  return num1 / num2


calculateDict = {"*": multiplication, "/": division, "+": addition, "-": subtraction}


if __name__ == '__main__':
  equationStr = raw_input("Enter a equation > ")
  calc(equationStr)



