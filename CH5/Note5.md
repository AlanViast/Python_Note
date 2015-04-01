# 第五章 Python基础

#### 1. 数字
1. 创建一个数字
    `a = 10`
2. 更新数字
    `a = 20`
3. 删除一个数字对象(只能删除变量对数字的引用)
    `del a`
4. 长整型, Python中的长整型的范围和机器支持的(虚拟)内存大小有关, Python支持小写的L做后缀, 但是建议使用大写的


#### 2. 浮点类型
1. Python中的浮点类型类似C的double类型, 是双精度浮点类型, 每个浮点型占8个字节(64位)


#### 3. 复数
1. 复数是不能单独存在的, 它们总是和一个值为0.0的实数部分一起来构成一个复数
2. 复数由实数部分和虚数部分构成.
3. 表示虚数的语法: real + imagj.
4. 实数部分和虚数部分都是浮点型
5. 虚数部分必须有后缀 j 或者 J

* 虚数的属性
    1. num.real: 表示复数的实部
    2. num.imag: 表示复数的虚部
    3. num.conjugate(): 返回该负数的共轭复数

#### 4. 操作符
1. 两种不同的类型进行运算的时候, 会将两种类型提升到同一种类型再进行计算, Python还提供了coerce()内建函数
    1. 如果一个操作数是复数的时候, 另一个操作数也会被转换成负数
    2. 如果一个操作数是浮点型的话, 另一个操作数也会被转换成浮点型
    3. 如果一个操作数是长整型的话, 另一个操作数也会被转换成长整型
    4. 否则两个操作数都是整型, 无需转换

