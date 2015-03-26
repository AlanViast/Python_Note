#!/usr/bin/env python
# -*- coding: utf-8 -*-

menu = '''
(S) 计算和
(A) 计算平均值
(X) 退出
'''

tempNumber = 0
numberList = []

while True :
    print menu
    choice = raw_input('输入你要使用的功能 > ')
    if choice == "X" :
        break

    for index in range(5) :
        tempStr = "Enter %s number" %(index + 1)
        number = raw_input(tempStr)
        numberList.append(number)
        tempNumber += int(number)

    if choice == "A" :
        print "数字 %s 的平均数是 %d" %(numberList, tempNumber / len(numberList))
    elif choice =="S" :
        print "数字 %s 的总和是 %d" %(numberList, tempNumber)


