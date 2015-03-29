# 第三章练习
====================

#### 1.为什么Python中不需要变量名额变量类型声明?
* 因为变量在赋值的时候才确定变量的类型

#### 2. 为什么Python中不需要声明函数类型?
* 函数没有定义返回的数据类型。 Python不需要提定返回值的数据类型；甚至不需要指定是否有返回值。实际上，每个Python函数都返回一个值；如果函数执行过return语句，它将返回指定的值，否则将返回None（Python 的空值）。(这部分答案是网上找到的)

#### 3. 为什么应当避免在变量名开始和结尾使用双下划线?
* 因为双下划线是系统定义名字

#### 4. Python中一行可以书写多个语句吗?
* 可以, 语句中间使用分号分隔

#### 5. Python中一行语句可以书写成多行吗?
* 可以, 末尾使用(\\)即可


#### 6. 变量赋值
1. 赋值语句 x, y, z = 1, 2, 3赋值后各是什么值?
    x = 1, y = 2, z = 3
2. 执行z, x, y = y, z, x后各是什么值?
    z = 2, x = 3, y = 1

#### 7. 下面那些是合法的Pyhon标志符? 如果不是, 请说明原因. 在合法的标志符中, 哪些是关键字?
1. 下面是合法的标志符
* int32
* printf
* _print
* self
* `__name__`
* true
* type
* thisIsAVar
* R\_U\_Ready
* Int
* do
* access
* _
* bool
* True

2. 下面的是关键字
* print
* if
* this

3. 下面是不合法的标志符
* $aving$
* big-daddy
* 2hot2touch
* 0x40L
* thisIsn`tAVar
* 40XL
* counter-1

#### 8. 修改输入提示符, 让代码看起来更简洁
* 略过. 查看markTextFile.py

#### 9. 在不同的操作系统中用Python查看 os.linesep的值


#### 10. 异常处理, 将两个文件都做异常处理
* 略过. 查看markTextFile.py 和 readTextFile.py

#### 11.修改readTextFile.py. 不要使用print只是输出NewLine, 并且在输出的时候去掉末尾的空格(使用strip函数)
* 略过. 查看readTextFile.py

#### 12. 合并源代码
* 略过, 查看TextFile.py

#### 13. 添加新功能, 让用户能编辑自己的文件




