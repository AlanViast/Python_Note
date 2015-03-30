# 第四章 Python对象

#### 1. 对象(所有Python对象拥有三个特性: 身份, 类型, 值)

* 身份: 没一个对象都有一个唯一的身份标识自己, 任何对象的身份可以使用内建函数 id() 来得到, 这个值可以被理解为对象的内存地址

* 类型: 对象的类型决定了对象可以保存什么值, 可以使用type()查看对象的类型, 所以type()返回的是对象而不是简单的字符串

* 值: 对象表示的数据项


#### 2. 标准类型
* Integer 整数
* Boolean 布尔类型
* Long Integer 长整型
* Floating point real number 浮点型
* Complex number 复数型
* String 字符串
* List 列表
* Tuple 元组
* Dictionary 字典

#### 3.其他内建类型
* 类型
    内建函数`type(obj)`会返回对象的类型, `type(type(obj))` 会返回一个类型的类型

* Null对象(None)
    Python有一种特殊的类型, 被称为Null对象或者NoneType, 他们仅有一个值`None`, 他们没有任何内建方法. None没有任何的属性, 他的布尔值总是False

* 文件
* 集合/固定集合
* 函数/方法
* 模块
* 类


* 布尔值, 所有的对象都可以用于布尔测试, 同类型的对象可以比较大小, 每个对象天生具有布尔True或者False值. 下列值都是False
    1. None
    2. False
    3. 0
    4. 0.0
    5. 0L
    6. 0.0 + 0.0j
    7. ""
    8. []
    9. ()
    10. {}





#### 4. 内部类型
* 代码
* 帧
* 跟踪记录
* 切片
* 省略
* Xrange
