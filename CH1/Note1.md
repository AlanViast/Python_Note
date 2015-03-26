# Python学习笔记第一章 #

#### 1.Python起源
Guido van Rossum 在1989年底创早了Python
1991年初, Python发布第一个公开发行版

#### 2. Python的特性
Python是可以升级的, 可扩展的, 可移植的.
Python是易学的, 可读性和易维护性强的. 有良好代码的健壮性
Python是面向对象的. 面向对象变成为数据和逻辑相分离的结构化和过程化添加了新的活力.
但是Python不像Java和Ruby仅仅只是面向对象的, 他还融入了多种编程风格.

#### 3. 解释性和(字节)编译性
Python是解释型语言, 和Java一样, Python实际上是字节编译的. 保持了解释型语言的优点

#### 4. Python的文件扩展名
Python的源文件通常是.py的,
当源文件被解释器加载或者显式地进行字节吗编译的时候会被编译成字节码.
由于调用解释器的方式不同, 源文件会被编译成带有.pyc和.pyo扩展名的文件

#### 5.Python运行方式
Python可以直接通过
$ python
运行,
命令行参数
-d     提供调试输出
-o     生成优化的字节码文件(生成.pyo文件)
-s     不导入site模块以在启动时查找Python的路径
-v     显示一些信息，比如导入某个包时显示包的信息
-m mod     将一个模块以脚本的方式运行
-Q opt     除法选项
-c  cmd     运行以命令行字符串形式提交的Python脚本
file     从给定的文件中运行Python见本

#### 6. Unix平台下运行Python
如果使用Unix平台, 可以在脚本第一行使用shell模式字符串("sh-bang").
`#!/usr/local/bin/python`
在#!后面写上Python的安装路径,一般都在/usr/local/bin或者/usr/bin目录下面.
如果你的系统有env,他会帮你在系统搜索路径中找到Python解释器
`#!/usr/bin/env python`
或者你的env位于/bin的话
`#!/bin/env python`
