# 第五章练习
====================

#### 1. 讲讲Python普通整型和长整型的区别
* 整型能存放四个字节的整数, 而Python的长整型能存放的值是根据计算机的虚拟内存而定的


#### 2. 操作符
1. 写一个函数, 计算并且返回两个数的乘积
2. 写一段代码调用这个函数, 并显示它的结果
```
#!/usr/bin/env python
'calculate two number\'s multiply result '

def multiply(number1, number2) :
    result = number1 * number2
    return result


if __name__ == '__main__' :
    result = multiply(10, 10);
    print result
```

#### 3.标准类型操作符, 写一段脚本, 输入一个测验成绩. 根据标准输出评分成绩
```
#!/usr/bin/env python
' show a student  score grade  '


def getGrade(score) :
    """ get a score's grade """
    if 100 < score :
        return "Is not a standard score"
    elif 90 < score <= 100 :
        return "A"
    elif 80 < score <= 90 :
        return "B"
    elif 70 < score <= 80 :
        return "C"
    elif 60 < score <= 70 :
        return "D"
    else :
        return "E"


if __name__ == '__main__' :
    scoreStr = raw_input("Enter a student score > ")
    score = int(scoreStr)
    grade = getGrade(score)
    print grade

```


#### 4. 取余, 判断给定的年份是否是闰年.
```
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

```


#### 5. 取余, 取一个小于1美元的金额, 然后计算可以换成最少多少枚硬币, 有1, 5, 10 25四种硬币
```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
coinList = [25, 10, 5, 1]

def minCoin(money) :
  if isinstance(money, float) :
    iMoney = int( float( money ) * 100 )
    count = 0
    statisticsCoin = []
    tempMoney = iMoney
    for i in coinList :
      tempCount,tempMoney = divmod(tempMoney, i);
      statisticsCoin.append(tempCount)
    print "%d 可以更换: %d 个25美分, %d个10美分, %d个5美分, %d个1美分" %(iMoney, statisticsCoin[0], statisticsCoin[1], statisticsCoin[2], statisticsCoin[3])

if __name__ == '__main__':
  money = raw_input("Enter money > ")
  minCoin(float(money))
```

#### 6. 算术, 写一个计算器, 只能使用split() 函数, 不能使用eval()
```
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
```


#### 7.营业税
```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def taxrate(wage) :
  return (wage - 3500) * 0.05

if __name__ == '__main__':
  wage = raw_input("Enter your wage > ")
  print taxrate(int(wage))

```


#### 8. 几何
1. 计算正方形和立方体
```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def getSquareArea(edge) :
  return edge ** 2;


def getSquareVolume(edge) :
  return edge ** 3;


if __name__ == '__main__':
  edge = raw_input("Enter a square edge > ")

  print "area: %d" %(getSquareArea(int(edge)))
  print "volume: %d" %(getSquareVolume(int(edge)))
```

2. 计算圆和球
```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

PI = 3.1415926

def getRoundArea(diameter) :
  """ get round area """
  radius = diameter / 2
  area = PI * (radius ** 2)
  return area


def getRoundVolume(diameter) :
  """ get round volume """
  radius = diameter / 2
  volume = (4.18879 * (radius ** 3))
  return volume



if __name__ == '__main__':
  diameter = raw_input("Enter a round diameter > ")

  print "Area: %s" %getRoundArea(float(diameter))
  print "Volume: %s" %getRoundVolume(float(diameter))
```

#### 9. 数值
1. 为什么17 + 32 = 49, 而017 + 32 = 47, 017 + 032 等于41?
* 因为0开头的数值代表八进制的数字

2. 为什么56l + 87l = 134L 而不是1342?
* 因为后面的l是小写的L

#### 10. 转换, 写一个函数来进行华氏度到摄氏度的转换(C = (F - 32) * (5 / 9))
```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

def change(fahrenheit) :
  celsuis = (fahrenheit - 32) * (5 / 9)
  return celsuis


if __name__ == '__main__':
  fahrenheit = raw_input("Enter a fahrenheit > ")
  celsuis = change(int(fahrenheit))
  print celsuis
```

#### 11. 取余
```
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
```

#### 12. 系统限制, 确认整型和长整型, 浮点型, 复数类型的范围
















