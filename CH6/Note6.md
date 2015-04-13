# 第六章 序列, 字符串, 列表和元组

#### 1. 标准类型操作符
1. 成员关系操作符(in, not in)
  obj [not] in seq

2. 序列类型操作符
  * seq[index]: 获得下标为index的元素
  * seq[index1: index2]: 返回下标从index1 到 index2 的元素集合
  * seq[start, end, step]: 返回start到end之间的元素, 每次间隔step位
  * seq * expr: 序列重复expr次
  * seq1 + seq2: 返回seq1 和 seq2的并集
  * obj in seq: obj是否在seq序列中
  * obj not in seq: obj是否不在seq序列中

#### 2. 内建函数(BIF)
1. 类型转换
  * list(iter): 把可迭代对象转换为列表
  * str(obj): 把obj对象转换成字符串(对象的字符串表示法)
  * unicode(obj): 把对象转换成Unicode字符串(使用默认编码)
  * basestring(): 抽象工厂函数, 其作用仅仅是为str和unicode函数提供父类, 所以不能被实例化, 也不能被调用
  * tuple(iter): 把一个可迭代对象换成一个元组对象

2. 序列类型可用的内建函数
  * enumerate(iter): 接受一个可迭代对象作为参数, 返回一个enumerate对象(同时也是一个迭代器), 该对象生成由iter每个元素的index值和item值组成的元组
  * len(seq): 返回seq的长度
  * max(iter, key=None) or max(arg1,arg2....., key=None): 返回一个iter或者(arg1, arg2.....)中的最大值, 如果指定了key, 这个key必须是一个可以传给sort()方法的, 用于比较的回调函数
  * reversed(seq): 接受一个序列为参数, 返回一个以逆序访问的迭代器
  * sorted(iter, func = None, key = NOne, reverse = False):接受一个可迭代对象作为参数, 返回一个有序的列表, 可选参数func, key, reverse的含义和list.sort()一样
  * sum(seq, init = 0): 返回seq和可选参数Init的总和, 效果等同于reduce(operator.add, seq, init)
  * zip([iter1, iter2, iter3....]): 返回每个iter1[0], iter2[0], iter3[0]形式的元组



#### 3. 字符串
1. 字符串的赋值
  aStr = "Hello World!"
  aStr[0] # 获得索引为0的
  del aStr

2. 标准类型操作符
```
aStr = "abc"
bStr = "lmn"
cStr = "xyz"

aStr < bStr
aStr != bStr
```

3. string模块
* dir
  ['Formatter', 'Template', '_TemplateMetaclass', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_float', '_idmap', '_idmapL', '_int', '_long', '_multimap', '_re', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'atof', 'atof_error', 'atoi', 'atoi_error', 'atol', 'atol_error', 'capitalize', 'capwords', 'center', 'count', 'digits', 'expandtabs', 'find', 'hexdigits', 'index', 'index_error', 'join', 'joinfields', 'letters', 'ljust', 'lower', 'lowercase', 'lstrip', 'maketrans', 'octdigits', 'printable', 'punctuation', 'replace', 'rfind', 'rindex', 'rjust', 'rsplit', 'rstrip', 'split', 'splitfields', 'strip', 'swapcase', 'translate', 'upper', 'uppercase', 'whitespace', 'zfill']

* string模块常用方法
```
import string
string.lowercase #所有小写字母
string.uppercase #所有大写字母
string.letters #所有字母
string.digits #所有数字
```

4. 普通字符串转换为Unicode字符串
* 'Hello' + u' '' + 'World' + u'!'!'

#### 4.
