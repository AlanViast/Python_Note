#!/usr/bin/env python
numberList = []

for index in range(3) :
    tempStr = "Enter %d number > " %(index + 1)
    number = raw_input(tempStr)
    numberList.append(int(number))

for i in range(len(numberList)) :
    for j in range(len(numberList) - i - 1) :
        if numberList[j] > numberList[j + 1] :
            temp = numberList[j]
            numberList[j] = numberList[j + 1]
            numberList[j + 1] = temp

print numberList
