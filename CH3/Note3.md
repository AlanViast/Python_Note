# 第三章 Python基础

#### 1. 语句和语法
* 井号(#), 表示之后的字符为Python注释
* 换行(\n), 标准的行分隔符(通常一个语句一行)
* 反邪线(\\),继续上一行
* 分号(;), 将两个一句放在同一行时用分号分隔
* 冒号(:), 将代码的头和体分开
* 语句(代码块), 用缩进去体现
* 不用的缩进深度分隔不同的代码块
* Python文件以模块的形式组织
* 代码规范, 建议使用4个空格去缩进

#### 2. 变量赋值
* 在Python中等号(=)是主要的赋值操作符(其他的是增量操作符)
* 增量赋值(Python不支持自增运算)
    1. +=
    2. -=
    3. *=
    4. /=
    5. %=
    6. **=
    7. <<=
    8.>>=
    9. &=
    10. ^=
    11. |=
* 多重赋值
    `a = x = y = 20`
* 多元复制(multuple), 采用这种方式复制时, 两边的对象都是元组, 所以建议使用`()`进行赋值, 这样可以使代码的可读性更强
    `x, y, z = 15, 12, 14`
    `(x, y, z) = (15, 12, 14)`
*

#### 3. 标志符
* 合法的Python表支付
    1. 第一个字符必须是字母或者下划线(_)
    2. 剩下的字符可以是字母和数字或下划线(_)
    3. 大小写敏感

* 关键字, Keywork模块中同时包含一个关键字列表, 和一个isKeyword()函数判断是否为关键字

* 内建(built-in), Python可以在任何一级的代码中使用内建的名字集合, 这些名字由解释器设置或者使用. 虽然built-in不是关键字, 但是应该当成系统保留字. built-in是`__builtins__`模块的成员

* 专用下划线标志符
    1. `_xxx` 不用`from module import *`导入
    2. `_xxx_` 系统定义名字
    3. `_xxx` 类内部私有变量名

* 基本风格指南
    1. 注释, 写合适的代码可以为每个人节省时间和精力, 请确保注释的准确性
    2. 文档, Python提供了`__doc__`特别变量来动态的获取文档字符串, 在运行时也可以进行
    3. 缩进, 建议使用4个缩进
    4. 选择标志符名称. 尽量使用简短而且能表示作用的名字.
    5. Python风格, 请看PEP文档

* 模块的结构和布局
    1. 起始行(Unix)
    2. 模块文档
    3. 模块导入
    4. 变量定义
    5. 类定义
    6. 函数定义
    7. 主程序

* 模块判断是否执行
    1. 如果模块是被导入的, `__name__`属性为模块名字
    2. 如果是被直接执行的, `__name__`属性为`__main__`

* 在主程序中书写测试代码
    测试代码仅当该文件被直接执行时运行, 我们应该在脚本执行的时候执行测试函数.

* 内存管理
    1. 变量无须事先声明
    2. 变量无须指定类型
    3. 程序员不用关心内存管理
    4. 变量名会被"回收"
    5. del 语句能直接释放资源

* 变量类型
    变量只有被创建和赋值后才能被使用

* 动态类型
    Python中的对象类型和内存占用都是运行时确定的. 也就是在赋值时, 解释器会根据语法和右侧操作数来决定新对象的类型.

* 内存分配
    Python解释器承担了内存管理的复杂任务

* 引用计数
    要保持追踪内存中的对象, Python使用了引用计数这一简单技术, 也就是Python内部记录着所有使用中的对象各有多少引用.

* 垃圾收集
    垃圾收集器是一块独立代码, 他用来寻找引用计数为0的对象. 它也会负责检查那些虽然引用技术不为0的但应该被销毁的对象(特定情节会导致循环引用)

#### 4. 使用局部变量代替模块变量
* 类似os.linesep这样的名字解释器需要做两次查询
    1. 查找os以确认它是一个模块
    2. 在这个模块总查找linesep变量

* 因为模块也是全局变量, 我们多消耗了系统资源, 如果在函数中频繁的使用这个属性, 我们建议用一个局部变量暂时保存该属性的值.



