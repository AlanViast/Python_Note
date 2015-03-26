#### 1. 安装Python, 请检查Python是否已经安装到你的系统上, 如果没有, 请下载并安装它.
    答案: 略过

#### 2. 执行Python. 有多少种运行Python的不同方法? 你喜欢哪一种? 为什么?
    答案:
        一种是在命令行执行python,
        第二种是python script.py执行脚本文件
        第三是使用IDE去开发执行
        第二种, 更适合项目的开发模式

#### 3. Python标准库
    a) 找到Python执行程序的安装文件和标准库的模块的安装位置.
          /usr/bin/python
          /usr/lib/python2.7
    b) 看看标准库里面的文件, 比如string.py. 这会帮助你适应阅读Python脚本

#### 4. 交互执行.
    启动你的Python交互器. 你可以通过输入完整的路径名来启动它.
    当然, 如果你已经在搜索路径中设置了他的位置,
    那么只输入它的名字(Python或者python.exe)就行了
    (你可以任选最适合你的Python实现方式, 例如命令行,
    图形用户接口/集成开发环境, Jython, IronPython 或者 Stackless).
    启动界面看上去就像本章描述的一样,
    一旦你看到>>>提示符就意味着解释器准备好要接搜你的Python命令了.
    直接输入print "Hello World"
    在Unix直接按下Ctrl+D会发送EOF信号终止Python解释器, DOS中直接按下Ctrl+Z退出

#### 5. 编写脚本, 同上面4一样,
>$ vim HelloWorld.py
```
#!/usr/bin/env python
print "Hello World !!!"
```

#### 6. 编写一个脚本, 使用print编写脚本, 在屏幕上显示你的名字, 年龄, 最喜欢的颜色与你相关的一些事情(背景, 兴趣, 爱好等)

>$ vim My.py
```
#!/usr/bin/env python
print "My name is Alan Viast"
print "24 old year "
print "like Red and play basketball"
```












