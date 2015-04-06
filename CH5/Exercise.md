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




























