# 第四章练习
====================

#### 1. Python对象, 与所有对象有关的三个属性是什么?简单描述下
    1. 身份: 每个对象都拥有一个id, ID相同的两个变量指向同一个对象
    2. 类型: 每个对象都是一种类型
    3.值: 每个对象都会有对应的值

#### 2. 类型不可更改(immutable)指的是什么? Python 哪些类型是可更改的(mutable), 哪些不是?
    * 不可更改是指对象的值一点确定了就不可以更改了
    * 列表和字典是可更改的.
    * 数字和元组还有字符串都是不可更改的.

#### 3. 类型, 那些类型是按顺序访问的, 它们和映射类型有什么区别?
    * 列表和元组还有字符串是按顺序访问的, 映射类型是按键访问的. 区别在与映射类型是无序的, 而列表, 元组和字符串都是有序的

#### 4. type()内建函数有什么作用? 它返回的对象是什么?
    * type()函数是用来判断对象的类型的, 返回指定对象的类型.

#### 5. str() 和 repr() 之间有什么不同? 哪一个等价与(``)操作符?
    * str()会返回格式良好的字符串, 而repr()会返回能代表对象的字符串(意思是能通过eval函数重新获得对象). repr()函数等同与``操作符

#### 6. 对象相等, 你认为type(a) == type(b) 和 type(a) is type(b)之间的不同是什么? 为什么会选择后者? 函数isinstance()和这有什么关系?
    * type(a) == type(b) 是判断值相等, 而type(a) is type(b)判断的是身份相等. 后者更严谨一点. isinstance判断一个对象是否是一个类的实例

#### 7. 内建函数dir(), 对types模块使用dir()内建函数, 并熟悉里面的类型.
    * BooleanType: 布尔类型
    * BuiltinFunctionType 内建函数类型
    * BuiltinMethodType 内建方法类型
    * ClassType 类类型
    * CodeType  代码类型
    * ComplexType 复数类型
    * DictionaryType 字典类型
    * EllipsisType 省略类型
    * FileType 文件类型
    * FloatType 浮点类型
    * FunctionType 函数类型
    * GeneratorType 生成器类型
    * IntType 整数类型
    * LambdaType lambda类型
    * ListType 列表类型
    * LongType 长整型类型
    * MethodType 方法类型
    * ModuleType 模块类型
    * NoneType None类型
    * ObjectType 对象类型
    * SliceType 切片类型
    * StringType 字符串类型
    * TracebackType 异常类型
    * TupleType 元组类型
    * TypeType (类型)的类型
    * UnboundMethodType
    * UnicodeType Unicode字符类型
    * XRangeType XRange类型

    * StringTypes
    * NotImplementedType
    * MemberDescriptorType
    * GetSetDescriptorType
    * InstanceType
    * FrameType
    * BufferType
    * DictProxyType
    * DictType

#### 8. 列表和元组有什么相同点? 有什么不同点?
    * 列表和元组都是顺序访问的, 都是可读而且有序的. 不同点在于元组是不可变的


#### 9. 实践
* 给定下面赋值, 请问下面输出是什么?
```
a = 10
b = 10
c = 100
d = 100
e = 10.0
f = 10.0

a is b    # True
c is d     # True
e is f      # False
```
*  因为Python会缓存 -0 - 100的整数
