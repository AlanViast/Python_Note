#### 1. 变量
* print 和字符串格式化操作符. 启动交互式解释器. 给一下变量赋值(字符串, 数值等)并通过输入变量名显示他们的值.再用print语句做同样的事情, 这两者有什么区别, 尝试用字符串格式操作符%, 并且熟悉它
```
tempStr = "test"
tempStr
print tempStr

print "my name is %s , %d years old" %("Tom", 24)

print "F%sC%s" %("u", "k")
```
* 直接输入变量输出字符串时会带单引号表示是一个字符串, 而print的时候则是直接输出


#### 2. 程序输出

> $ vim Test.py

```
#!/usr/bin/env python
1 + 2 * 4
```

1. 你认为这段脚本用来做了什么?
* 计算 1 \+ (2 \* 4)的值

2. 你认为这段脚本会输出什么?
* 不会输出

3. 将上面的代码保存到脚本, 并且执行它. 看下是否和预期一样, 为什么一样/不一样
* 一样, 因为在只有在解释器里面计算才会直接输出结果, 在脚本中则不会

4. 这段代码单独执行和在解释器中有什么不同.
* 在解释器中直接输入会输出计算后的结果, 而脚本文件则不会

5. 如何改进这个脚本, 以便它和你想象的一样工作?

> $ vim newTest.py

```
#!/usr/bin/env python
result = 1 + 2 * 4
print result
```



#### 3. 数值和操作副
* 打开解释器, 使用Python对两个数字任意类型进行加, 减, 乘, 除运算然后取余操作符来得到两个书相除的余数, 最后用乘方求A数和B数的次放
```
b = True
f = False
print b + f
print b - f
print b * f
print b / f

number1 = 64
number2 = 43
print number1 + number2
print number1 - number2
print number1 * number2
print number1 / number2
print number1 % number2
print number1 ** number2
```
* Boolean 类型计算的时候会被转换成数值, True是1, False是0

#### 4. 使用raw_input()获得用户输入
1. 写一个脚本, 使用raw_input()内建函数从用户输入获得一个字符串, 然后显示用户输入的字符串

> $ vim Input.py

```
#!/usr/bin/env python
tempStr = raw_input("Enter a string > ")
print tempStr
```

2. 同上, 但是将输入的字符串转换为整数
```
#!/usr/bin/env python
tempStr = raw_input("Enter a number > ")
number = int(tempStr)
print "you enter a number is > %d" %(number)
```


#### 5. 循环和数字
1. 分别写一个循环, 用for 和 while
```
for x in range(10):
    print x,

x = 0
while( x < 10):
    print x,
    x += 1
```

2. 使用一个while循环输出0～10, 而不是0～9
```
x = 0
while( x < 11) :
    print x,
    x += 1

x = 0
while( x < 10):
    print x,
    x += 1

print x
```
3. 同上, 但是这次用range()内建函数
```
for x in range(11):
    print x,

```

#### 6. 条件判断
* 判断一个数是否为整数
```
#!/usr/bin/env python
num = raw_input('Enter a number > ')
try:
    number = int(num)
    if number == 0 :
        print "number is zero"
    elif number == abs(number):
        print "number is a integer"
    else :
        print "number is negative number"
except Exception, e:
    print "you enter not a number"
```

#### 7. 循环和字符串
1. 接受用户输入一个字符串, 然后逐一输出单个字符
```
tempStr = raw_input("Enter a string > ")

for ch in tempStr:
    print ch,

tempStrLength = len(tempStr)
x = 0
while x < tempStrLength :
    print tempStr[x],
    x += 1
```


#### 8. 循环和操作符
1. 创建包括五个值的列表或者元组, 然后输出他们的和, 分别用for 和 while实现
```
sum = 0
for x in range(5):
    temp = "Enter %s number > " %(x + 1)
    tempStr = raw_input(temp)
    number = int(tempStr)
    sum += number

print sum

sum = 0
x = 0
while x < 5 :
    temp = "Enter %s number > " %(x + 1)
    tempStr = raw_input(temp)
    number = int(tempStr)
    sum += number
    x += 1

print sum
```

#### 9. 循环和操作符
1. 创建一个包含五个数的列表或者元组. 暑促他们的平均值

```
sum = 0.0
for x in range(5):
    temp = "Enter %s number > " %(x + 1)
    tempStr = raw_input(temp)
    number = float(tempStr)
    sum += number

print sum / 5

sum = 0.0
x = 0
while x < 5 :
    temp = "Enter %s number > " %(x + 1)
    tempStr = raw_input(temp)
    number = float(tempStr)
    sum += number
    x += 1

print sum / 5
```

#### 10. 带循环和条件判断用户输入
1. 使用raw_input()内建函数接受用户输入一个1～100的数字, 如果用户输入的数满足这个条件则显示退出否则显示一个错误信息让用户继续输入

```
num = int(raw_input("Enter a number in 1 ~ 100 > "))

while num != 59 :
    print "Enter number not correct"
    num = int(raw_input("Enter a number in 1 ~ 100 > "))
else :
    print "Enter number correct"
```


#### 11.做一个带文本菜单的程序, 完成 (1)取五个数的和, (2)取五个数的平均值, (X)退出程序

```
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
```



#### 12. dir()内建函数
* 启动Python解释器, 执行`dir()`
* 输出: `['__builtins__', '__doc__', '__name__', '__package__']`

* 执行`dir()`不要带括号会输出什么, 为什么会输出这些?
* 输出: `<built-in function dir>`, built-in 表示内建, funcion dir表示函数名字

* 执行`type()`内建函数是下, 输入type(dir)再试下.
* `type(dir)` 输出来 `<type 'builtin_function_or_method'>`, 表示dir是一个内建函数. `type(“str”)`

* 通过`dir.__doc__`可以访问到dir内建函数的文档. 可以用`print dir.__doc__`输出文档

#### 13. 使用`dir()`找出更多sys模块中更多的东西
* 打开解释器, 执行`dir()`, 使用`import sys`导入sys模块. 然后执行`dir()`,确认sys模块是否导入了.然后就能看到sys所有属性.

* 显示sys模块的版本号属性及平台变量. 记住在属性前一定要加sys, 这个属性是sys模块的. 其中version变量存放着Python解释器版本. platform属性则包含你运行Python时使用的计算机平台信息

* 最后调用sys.exit()函数, 这是一种热键之外的另一种推出Python解释器的方式

#### 14. 操作符优先级和括号分组.
* 重写2.4小节中的print语句中的里的算数运算式. 试着中添加适合的括号以便能让他正常工作
```
print -2 * ( 4 + 3 ) ** 2
print -2 * ( 4 + 3 ** 2 )
print ( -2 * ( 4 + 3 )) ** 2
```

#### 15. 元素排序
* 让用户输入三个值, 保存到一个列表中, 然后从小到大排序.
```
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

```

* 同上, 排序顺序为从大到小
```
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

```


#### 16. 将上面的练习都改成脚本文件的形式, 然后看下是否能正常运行
