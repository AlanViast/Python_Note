# Python学习笔记第二章 #


#### 1. 解释器下的技巧 ####
1. 在脚本文件中要查看一个变量的值需要打印出来, 在解释器中可以直接输入变量名即可输出
2. 输入_表示最后一个表达式的值


#### 2. 字符格式化操作符 ####
%s  表示一个字符串来替换
%d  则是整数替换
%f  表示一个浮点数
```
print "%s is number %d" %("Python", 1)
```



#### 3. 输出重定向 ####
从 **Python 2.0** 开始, Print语句也支持将输出重定向到文件, 使用符号>>来重定向输出
```
import sys
print >> sys.stderr, "Fatal error: invalid input !!!"
// 下面是重定向到日志文件的例子
logfile = open('/tmp/mylog.txt', 'a')
print >> logfile, "Fatal error: invalid input! "
logfile.close()
```


#### 4.程序输入 ####
* 通过raw_input()内建函数能读取标准输入, 获取用户输入的内容
```
username = raw_input("Enter your name")
print 'Your name is ', username
```
* 通过int()内建函数能将用户的输入转换成整数性
```
age = raw_input('Enter your age')
print 'You %d years old' % (int(age))
```



#### 5. 从交互器获取帮助 ####
* 在学习过程中， 如果遇到一个陌生的函数, 可以调用内建函数`help(raw_input)`去获得相应的帮助

#### 6.注释 ####
1. Python单行注释使用#开头, #号后面的字符会被编译器省略
2. 文档注释, Python中的文档注释用两个"包括, 文档注释可以用来生成文档
```
def foo() :
    "This is a doc string"
    return True
```


#### 7. 操作符 ####
1. 运算操作符( \+, \-, \*, /, //, %, \*\* )
加减乘除和取余都是正常运算符, 但是Python有两种除法, //会对浮点除法进行四舍五入, /会进行地板除运算. \*\*运算的优先级最高, (3 \*\* 2) 表示3的2次方

2. 比较运算符 ( <, <=, >, >=, ==, !=, <>)
Python支持两种  **不等于**  比较符, 分别是!=和<>, 建议使用前者

3. 逻辑运算符( and, or, not)


#### 8. 标识符和变量 ####
* Python中的变量名只支持 **字母**, **数字**, **下划线(_)**. 开头只能使用字母或者下划线

* 而且Python中的变量名是大小写敏感的

* Python是动态语言, 所以不需要声明变量的类型, 变量类型在复制的时候被初始化

* Python不支持增量赋值, 所以不支持\-\-n和 \+\+n.


#### 9. 数字 ####
* Python有五种基本数字类型, 其中三种是整型类型
    1. int
    2. long
    3. bool
    4. float
    5. complex

#### 10. 字符串 ####
1. Python中字符串被定义为引号之间字符的集合.
2. Python支持使用成对的单引号, 双引号, 三引号(三个单引号或者三个双引号)
3. 字符串可以使用索引操作符([])和切片操作符([:])获取子字符串
4. 字符串第一个索引是0, 最后一个索引是-1.
5. 使用\+对字符拼接, 使用\*用于字符串重复

```
tempString = "双引号字符"
print tempString
tempString = '单引号字符'
print tempString
tempString = """三引号字符"""
print tempString


tempString = "Love"
print tempString[2]

tempString = "this is very cool"

print tempString[8 : 12]
print tempString[13:]
print tempString[:5]
print tempString[-12: -10]

print '''Hello, ''' + tempString

print "Hello, " * 2
```


#### 11. 列表与元组 ####

* 可以将列表和元组当成普通的数组, 它能保存任意对象, 和数组一样都是从0开始索引访问元素.
* 列表元素用 `[]` 包裹, 元素的个数以及元素的值可以改变
* 元组元素用 `()` 包裹, 不可以更改. 可以把元组看作一个只读的列表
* 和字符串一样, 元组和列表都通过切片`([]和[:])`可以得到子集

```
tempList = [1, 2, 3, 4]
print tempList

print tempList[2]
print tempList[2:]
print tempList[:3]

tempTuple = ('this', 'is', 'a', 'tuple')
print tempTuple
print tempTuple[2]
print tempTuple[2:]
print tempTuple[:3]
```


#### 12. 字典 ####
* 字典是Python中的映射数据类型, 原理类似与关联数组或者哈希表, 由键-值(key-value)
* 几乎所有的Python对象都可以作为键, 不过数字和字符串最常用
* 值可以是任意类型的对象, 字典元素用`{}`包裹

```
aDict = {'host': 'baidu.com', 'port': 80}
print aDict['host']
print aDict['port']

for key in aDict:
    print key, aDict[key]
```
#### 13. if语句 ####
* 标准的 if 语句, expression是表达式, 如果表达式返回的结果为True则执行if\_suite, 如果在有elif的情况下则执行elif后的expression.否则执行else\_suite
```
if expression:
    if_suite

if expression:
    if_suite
else:
    else_suite

if expression:
    if_suite
elif expression:
    elif_suite
else:
    else_suite
```

#### 14. for循环和range()内建函数 ####
* Python中的for循环和传统的for循环不太一样, 它像shell脚本里面的foreach迭代一样, Python的for接受一个可迭代对象(例如序列或者迭代器)作为参数.

* 内建函数range(int)会生成并返回一个整数型的列表

* 字符串类型也是可迭代的类型

* len()内建函数会返回字符串的长度

* 一般循环都是循环索引或者循环元素, 所以在Python 2.3之后新增 `enumerate()` 函数, 它会返回一个元组, 第一个值是索引, 第二个值是元素

```
print 'I like to use Internet for:'
for item in ['I', 'Love', 'You'] :
    print item,
\#item后面的逗号使用来分割元素的, 会用一个空格来分割
print  #用来输出一个换行符

for eachNum in [0, 1, 2, 3] :
    print eachNum,

for eachNum in range(4):
    print eachNum,

tempStr = "Test"
for ch in tempStr:
    print ch,

for index in range(len(tempStr)):
    print tempStr[index],


for index, ch in enumerate(tempStr):
    print index, ch
```

#### 15. 列表解析 ####
* 这个功能可以让你在一行代码中使用一个for循环将所有值放到一个列表中

```
squared = [ x ** 2 for x in range(10)]
print squared

filter = [ x ** 2 for x in range(9) if not x % 2]
print filter
```

#### 16. 文件和内建函数open(), file() ####
* 通过`handle = open(fileName, access_mode = 'r')`能打开一个文件
    1. fileName是我们希望打开的文件路径
    2. access_mode是访问的模式, 默认为'r'
        * 'r'表示读取
        * 'w'表示写入
        * ’a'表示添加
        * '+'表示读写
        * 'b'表示二进制访问

* 通过open成功会返回一个文件的句柄. 后续的文件操作都会通过文件的句柄进行.可以调用其`readline()`和`close()`方法

* file()和open()函数都是一样的, 只是file更语义化.

```
fileName = raw_input("Enter file name:")
fObj = open(fileName, 'r')
for eachLine in fObj:
    print eachLine,
fObj.close()
```

#### 17. 属性和函数 ####
* 属性可以是简单的数据, 也可以是可执行对象, 比如函数和方法

* 通过`object.attribute`可以访问属性

* 函数通过`()`调用, 函数必须在调用前定义, 如果函数没有return语句, 则自动返回None对象

* Python是通过引用调用的, 所以函数内对参数的改变会影响到原始对象(只有可变的对象会, 对不可变的对象则类似按值调用).

* 函数的参数只能有一个默认参数, 表示当调用函数的时候没有提供这个参数, 则取默认值



```
def function_name([arguments]) :
    'optional documentation string'
    function_suite

def foo(debug = True):
    'determine if in debug mode with default argument'
    if debug :
        print "in debug mode"
    print 'Done'
```

#### 18. 错误和异常 ####
* 编译时编译器会检查语法错误, 但是Python也允许在程序运行时检测错误, 所以我们需要自己处理运行时的错误

* 捕获错误可以通过try-except语句, 将可能会发生错误的代码放在try代码块中, 将处理异常的代码放在except代码块中

```
try:
    fileName = raw_input('Enter file name:')
    fObj = open(fileName)
    for eachLine in fObj:
        print eachLine,
    fObj.close()
except IOError, e:
    print 'file open error', e
```

#### 19. 类 ####
* 类是面向对象的核心, 他们提供了创建 "真实" 对象的蓝图

* 类在创建的时候会调用`__init__()`方法

* self是类实例自身的引用,
```
\#定义一个类
class ClassName(base_class[es]):
    "optional document string"
    static\_member\_declarations
    method\_dealartions

class Person(object):
    'Person Object'
    name = "",
    age = 20
    def \_\_init\_\_(self, nm="nobody"):
        self.name = nm
        print "Created a person object"

    def sayHi():
        print 'Hello, my name is %s' %(self.name)

```
#### 20. 模块 ####
* 模块是将有关系的Python代码组织到一个个独立文件中, 模块可以包含可执行代码, 函数, 类
* 当你创建了一个Python源文件后, 模块名字就是你的文件名(不带后缀.py的)
* 可以通过`import module_name`的方式导入一个模块


#### 21. PEP ####
* PEP(Python Enhancement Proposal)是一个Python增强提案.

#### 22. 使用的函数 ####
* dir([obj]): 显示对象的属性, 如果不提供参数则显示全局变量的名字
* help([obj]): 以蒸汽的形式显示对象的文档字符串, 如果不提供参数则进入交互帮助模式
* int(obj): 将对象转换成整数
* len(obj): 返回对象的长度
* open(fn, mode): 按mode的形式打开一个文件
* range([start,] stop[, step]): 返回一个整数列表
* raw_input([str]): 等待用户输入, str显示输入提示
* str(obj): 将一个对象转换成字符串
* type(obj): 返回对象的类型



