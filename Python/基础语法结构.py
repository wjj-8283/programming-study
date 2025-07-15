# 错误示范的问题所在可在问题选项卡中查看哦

# Python 3默认采用UTF-8编码，所有的字符串均为unicode字符串
# 也可以为源码文件指定不同的编码：
# -*- coding:utf-8 -*-
# utf-8可以改为其他的编码，如gbk、ansi等等

# 标识符主要用于变量名、函数名、类名等等
"""
标识符规范
1.第一个字符必须为字母或者下划线“_”
2.标识符的其他部分由字母、数字和下划线“_”组成
3.标识符对大小写敏感，大小写不同标识符不同
4.不能使用保留关键字
"""
'''
标识符命名规范：
1.尽可能使用有意义的单词作为标识符
2.模块名尽量短小，全部使用小写字母，可以使用下划线分隔多个字母
3.包名尽量短小，全部使用小写字母，不推荐下划线
4.类名采用Pascal风格，如MyClass
5.模块的内部的类采用下划线+Pascal风格类名组成，例如：在MyClass内部的类_InnerMyClass
6.函数、类的属性和方法的命名，全部使用小写字母，多个字母之间使用下划线分隔
7.常量命名时采用全部大写字母，可以用下划线
8.使用单下划线开头的模块变量或函数是受保护的，无法使用from xxx import语句导入
9.使用双下划线开头的实例变量或方法是类私有的
10.以双下划线开头和结尾的函数或变量名是Python的专用标识，例如：__init__()表示初始化函数
'''
# 例如：以下为合法标识符
age = 25
user_name = "Alice"
_total = 100
MAX_SIZE = 1024
中文 = "Chinese" # 中文字符也可用作标识符，但是不推荐
π = 3.141592653589793263 # 非ASCII字符也可以用作标识符，但是不推荐
# 错误示范
2nd_place = "silver"    # 错误：以数字开头
user-name = "Bob"       # 错误：包含连字符，会被Python识别为减法运算
class = "Math"          # 错误：使用关键字
$price = 9.99          # 错误：包含特殊字符
for = "loop"           # 错误：使用关键字

# 保留关键字
# 查询：
import keyword
print(keyword.kwlist)
# 结果：
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
# 'try', 'while', 'with', 'yield']
# 保留关键字不得用于标识符

# 行与缩进
# Python使用缩进来表示代码块和程序结构，不需要大括号{}
# 缩进空格数是可变的，但是同一个语句块必须包含相同的缩进空格数
# 正确示范：
if True:
  print("True")
else:
  print("False")
# 错误示范：
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
  print(False)

# 多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠\来实现多行语句
# 例如：
item_1 = 1
item_2 = 2
item_3 = 3
total = item_1 + \
        item_2 + \
        item_3
print(total)

# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：
import sys; x = 'wjj'; sys.stdout.write(x + '\n')
# 在[]，{}，或()中的多行语句不需要使用反斜杠，例如：
total = ['item_1', 'item_2', 'item_3', 
         'item_4', 'item_5']

# 变量赋值特殊用法：
# Python允许你同时为多个变量赋值。例如：
a = b = c = 1
# 也可以为多个对象指定多个变量。例如：
a, b, c = 1, 2, "wjj"
