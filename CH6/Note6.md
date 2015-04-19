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

#### 4. 字符串操作
1. 格式化操作符(%)
* %c : 转换成字符(ASCII码值, 长度为1的字符串)
* %r : 优先使用repr()函数进行字符串转换
* %s : 优先使用str()函数进行字符串转换
* %d / %i : 转换成有符号十进制数字
* %u : 转换成无符号十进制数字
* %o : 转成无符号八进制数字
* %x / %X : 转换成无符号十六进制(x/X代表转换后的十六进制字符的大小写)
* %e / %E : 转换成科学计数法(e/E控制输出e/e)
* %f / %F : 转换成浮点型(小数部分自然截断)
* %g / %G : %e 和 %f, %E 和 %F 的简写
* %% : 输出%

2. 格式化操作符辅助符
* * : 定义宽度或小数点精度
* - : 用作左对齐
* + : 在正数前面显示加号(+)
* <sp> : 在正数前面显示空格
* # : 在八进制前面显示零('0'), 在十六禁止前面显示'0x'或者'0X'(取决与用的是'x'还是'X')
* 0 : 显示数字前面填充'0', 而不是默认的空格
* % : '%%'输出单一的的'%'
* (var) : 映射变量(字典参数)
* m.n : m是显示的最小总宽度, n是小数点后的位数(如果可用的话)

3. Demo
```
print "%x" %108
print '%X' %108
print '%#x' %108
print '%#X' %108


print '%f' %1234.567890
print '%.2f' %1234.567890
print '%E' %1234.567890
print '%e' %1234.567890
print '%g' %1234.567890
print '%G' %1234.567890
print '%e' %(1111111111111111111L)


print '%+d' %4
print '%-d' %-4
print 'we are at %d%%' %100
print 'Your host is : %s' %'earth'
print 'Host: %s\tPort: %d' %('mars', 80)
num = 123
print 'Dec: %d/ort: %#o/hex: %#X' %(num, num, num)
print "MM/DD/YY = %02d/%02d/%d" %(2, 15, 67)
w, p = 'Web', 'Page'
print "http://www.yyy.zzz/%s/%s.html" %(w, p)
```

4. 字符串模板, substitute() 和 safe_substitute()一样, 但是前者缺少key的情况下会报错, 后者在缺少key的情况下直接输出内容
```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from string import Template

sTemplate = Template('There are ${howmany} ${lang} Quotation Symbols')
print sTemplate.substitute(lang = 'Python', howmany = 3)

print sTemplate.safe_substitute(lang = 'Python')
```

5. 原始字符串
  * 通过\n可以输出一个换行, 当需要输出文本"\n"时候, 可以使用 `r"\n"`, r表示该字符串不转义
  * 原始字符串查找
  ```
  import re
  m = re.search("\\[rtfvn]", r"Hello World\n")

  if m is not None :
    print m.group()

  m = re.search(r"\\[rvfn]", r"HelloWorld\n")

  if m is not None :
    print m.group()
  ```

6. Unicode字符
  * 通过`u"Hello World"`可以输出Unicode字符
  * 如果要使用原始字符串和Unicode字符的情况下, u操作符必须在原始字符串操作符号前面, 如`ur"Hello \n World"`

7. 字符串的内建函数(BIF) :
  * cmp() : 字符串比较操作符号,`cmp(str1, st2)`, 字符串之间的比较是通过ASCII码值进行比较的
  * len() : 计算字符串长度
  * max() 和 min() : 计算两个字符串的最大值或者最小值他(也是通过ASCII码值作比较)
  * enumerate() : 返回一个索引和值组成的元组对象迭代器
  * zip() : 将两个序列对象, 组成一个元组迭代数组, 只取最短长度的

8. 字符串类型函数
  * raw_input([message]) : 函数接受一个用户的标准输入, 返回用户输入的字符串
  * str() 和 unicode() : 都是工厂函数, 就是说产生所对应的类型对象, 他们接受一个任意类型的对象, 然后返回一个描述该对象的字符串
  * chr(), unichr() 和 ord() : chr()返回一个范围在range(256)之间的整数作参数, 返回一个对应的字. unichr()跟它一样, 但是返回一个unicode字符, ord()返回一个ASCII码值

9. 特殊字符串和控制字符



