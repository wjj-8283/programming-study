# import module as mo和from module import function：导入外部模块
# module为导入的模块名称，mo为自定义的模块简称，function为模块的内部功能/函数，若为*则表示导入所有可用的功能和函数
# 通过import语句导入的模块调用模块内部的函数需要使用如下格式：module.function()，若有自定义的函数简称则为mo.function()
# 而from ... import就直接使用对应的函数名，不需要前缀
# 例如：
import keyword
print(keyword.kwlist)
# 输出Python保留字

import random as ra
print(ra.randint(30,100))
# 生成30和100之间的随机数并输出

from sys import path
print("path:",path)
# 打印Python环境路径

# print()：用于在终端输出内容
# 语法：
# (function) def print(
#     *values: object,
#     sep: str | None = " ",
#     end: str | None = "\n",
#     file: SupportsWrite[str] | None = None,
#     flush: Literal[False] = False
# ) -> None
# values：类型不限，在终端输出的内容，可以输出多个内容，中间用逗号隔开
# sep：字符串类型，不同内容之间的分隔符，默认为一个空格
# end：字符串类型，输出内容的末端的内容，默认为换行符
# file：后面接打开的文件（open函数打开文件），所有的内容会写入file后的文件，默认为空
# flush：后接bool类型的参数，若为True就强制刷新缓冲区，强制显示待加载的字符串，默认为False
# print()没有返回值
# 示例：
print("a", "b", "c")
# a b c

print('a', 'b', 'c', 123, 234, 345, sep="@")
# a@b@c@123@234@345

print('12345', end="")
print('6789')
# 123456789

print(123, 567, "wjj", end="",file=open("Python/text.txt", "w"))
# 终端无输出，Python文件夹中text.txt中会写有：
# 123 567 wjj

import time
print("Loading",end="")
for i in range(20):
  print('.', end="", flush=True)
  time.sleep(0.5)
# 动态的加载，每0.5s多一个点，共20个

back = print("abc")
print(back)
# abc
# None（没有返回值）

# input()：用于在终端中进行内容输入
# 语法：
# (function) def input(
#     prompt: object = "",
#     /
# ) -> str
# prompt：字符串类型，输入前的提示语，默认值为空
# 返回值为输入的值,字符串类型
# 例如：
name = input('Name？')
print("Hello", name)
# 终端将会输出Hello+你输入的内容

# type()：用于返回括号中的内容属于的类或者返回新的类型对象
# 语法：(class) type
# type(object) -> 返回object的数据类型
# type(name, bases, dict, **kwds) -> 返回新的类型对象（这个用法不常用）
# 例如：（请在Interactive Window中逐行执行）
type(12)                   # int
type(12.0)                 # float
type("12")                 # string
type([1,2,3])              # list
type((1,2,3))              # tuple
type(True)                 # bool
type({1,2,3})              # set
type({"uhduw":"hello"})    # dictionary

# isinstance()：用于判定给定的内容是否属于某一个类
# 语法：def isinstance(
#     obj: object,
#     class_or_tuple: _ClassInfo,
#     /
# ) -> bool
# 该函数用于判断给定的obj是否是给定的class_or_tuple中的类型或其子类类型，返回bool类型
# class_or_touple可以是类，也可以是由类组成的元组
# isinstance(A,(B,C,D))等价于isinstance(A,B) or isinstance(A,C) or isinstance(A,D)
# isinstance()会认为子类是一种父类类型，会考虑继承，但是type()不会
# 例如：(请在Interactive Window中逐行执行）
isinstance("Hello",str)                 # True
isinstance(123,str)                     # False
isinstance("hello",(str,int,float))     # True
isinstance(True,int)                    # True，因为在Python中，bool类型为int类型的子类
type(True) == int                       # False,因为type()不考虑继承

# del：用于删除对象引用
# 语法：del var1[, var2[, var3[...., varN]]]
# del语句可以用于删除一个或者多个对象的引用
# 例如：（以下代码请逐行在Interactive Window中运行，并打开Jupyter Variables显示）
a = 1
b = 2
c = 3
d = 4
del a
del b,c,d

# len()：用于获取内容的数量
# 语法：def len(
#     obj: Sized,
#     /
# ) -> int
# 内填可以被计数的内容（元组、列表、字典、集合、字符串，数字类型不行），
# 若为字符串则返回字符数，若为元组、列表、字典、集合则返回元素数
# 例如：（请在Interactive Window中逐行执行下方的代码）
len("Hello World.你好，世界")         # 17
len(['wjj',12,[123,234,345]])       # 3
len(('wjj',12,45,23.0))             # 4
len({"123":124,"wjj":1024})         # 2
len({112,123,123,124,124})          # 3

# split()：将字符串拆分成列表
# 语法：string.split(splitter)
# string为待拆分的字符串，splitter为待拆分的字符串的分隔符
# 示例：
string1 = 'Hello World'
string2 = 'I like You. You like me.'
print(string1.split(" "))     # ['Hello', 'World']
print(string2.split(". "))    # ['I like You', 'You like me.']

# join()：将列表中的字符串在一定的分隔符下合并
# 语法：splitter.join(list)
# splitter为期望的分隔符，list为待合并的字符串组成的列表
# 示例：
list = ['I','Love','You']
print(" ".join(list))   # I Love You
print("❤️".join(list))  # I❤️Love❤️You

# id()：用于返回对象的身份标识
# 语法：def id(
#     object: object,
#     /
# ) -> int
# 返回对象的身份标识，该标识在同时存在的对象中保证唯一。在CPythonhon中，该标识为对象内存地址
# 例如：
a = 1
b = 1
c = 1
print(id(a))
print(id(b))
print(id(c))