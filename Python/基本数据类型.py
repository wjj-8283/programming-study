# Python基本数据类型有6个，分别为数字（numbers）、字符串（string）、布尔类型（bool）、列表（list）、元组（tuple）、集合（set）、字典（dictionary）、字节数组类型（bytes）
# 其中可变的数据类型有：列表、集合、字典
# 不可变数据类型有：数字、字符串、元组、字节数组类型、布尔类型

# 数字类型
# 数字一共有四种类型：整数（int）、浮点数（float）、布尔型（bool）和复数（complex）
# 示例：
123 # 十进制整数
0x2AF38 # 十六进制整数，x可换为X
0o737243 # 八进制整数，o可换为O
0b010111010101 # 二进制整数
3.1415926 # 浮点数
32.3e+18 # 浮点数（科学计数法），e可换为E
-32.54e100 # 浮点数（科学计数法），e可换为E
True # 布尔型，表示真，等价于1
False # 布尔型，表示假，等价于0
3+4j # 复数
complex(3,4) # 复数，与上面等效
# 数字的运算：
5 + 4   # 加法
4.3 - 2 # 减法
2 / 4   # 除法，得到一个浮点数
2 // 4  # 除法，得到一个整数
17 % 3  # 取余
2 ** 5  # 乘方

# 字符串
# Python中单引号'与双引号"使用完全相同
# 使用三引号（'''或"""）可以指定一个多行字符串
# 转义符是\
# 反斜杠可以用于转义，使用r可以让反斜杠不发生转义
# 按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复
# Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
# Python中的字符串不能改变,因此不能使用str[index] = "string"的形式的代码更改字符串的内容，若执行会出现：TypeError: 'str' object does not support item assignment
# Python没有单独的字符类型，一个字符就是长度为1的字符串
# 例如
'字符串'
"这是一个句子。"
"""这是一个段落，
可以有多行组成"""
# 字符串操作
# 取一个字符：str[number]
# 其中number为字符的索引
# 切片：str[start:end:sep]
# 其中start为切片开始的索引，end为切片结束的索引（不含该字符），sep为步长，当sep为负数时，表示反向读取
# 例如：
str = '123456789'
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[:-1])            # 输出从第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
print('hello\nwjj')        # 使用反斜杠(\)+n转义换行符
print(r'hello\nwjj')       # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# 常见的转义字符：
# \n：换行符
# \t：横向制表符
# \\：一个反斜杠
# \'：字符串中的单引号
# \"：字符串中的双引号
# \r：回车
# \b：退格
# \f：换页
# \v：垂直制表符
# \a：响铃
# \0或\000：空白字符
# \oyy：八进制数yy代表的字符
# \xyy：十六进制数yy代表的字符
# \uxxxx或\Uxxxx：Unicode字符表中编号为xxxx的字符

# 布尔类型
# 布尔类型即True或False，是一种用来表示真或假的数据类型
# 主要用于控制程序流程，比如判断某一条件是是否成立，或在某一条件下执行某一代码
# 特点：
# 1.布尔类型是整数类型的子类，比如True等价于1，False等价于0
# 2.布尔类型可以与其它类型进行比较，在比较时Python会将True视为1，False视为0
# 3.布尔类型可以和逻辑运算符连用，用来组合多个布尔表达式，结果会生成新的布尔值
# 4.布尔类型可以被转换成其它类型，转换时True会被视为1，False会被视为0
# 5.可以使用bool()将其他的数据类型转换为布尔类型，在转换时，以下的数据会被视为False，其他的均会被转换为True：
# None，False，零（0，0.0，0j），空序列（”“，()，[]），空映射（{}）
# 示例：
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

print(int(True))             # 1
print(int(False))            # 0
print(isinstance(True,int))  # True
print(isinstance(False,int)) # True

print(bool(0))         # False
print(bool(42))        # True
print(bool(''))        # False
print(bool('Python'))  # True
print(bool([]))        # False
print(bool([1, 2, 3])) # True

print(True and False)  # False
print(True or False)   # True
print(not True)        # False

print(5 > 3)  # True
print(2 == 2) # True
print(7 < 4)  # False

if True:
    print("This will always print")
    
if not False:
    print("This will also always print")
    
x = 10
if x:
    print("x is non-zero and thus True in a boolean context")

# 列表
# 列表用中括号括起来，中间的各个元素用逗号隔开
# 列表中的元素的类型不受任何限制，且允许混合
# 列表也可以像字符串一样被索引和切片，索引方式和字符串类似
# 同字符串一样，可以用 + 连接两个列表，可以用 * 重复列表中的内容
# 列表是可变的数据类型，可以对列表中的某一元素进行修改，也可以对多个元素进行修改
# 列表的其他操作请见列表.py
# 列表的示例：
["string",12,12.0,True,["new_list",120,60]]
# 示例程序：
# 列表的切片、重复、合并
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]  # 定义一个列表
tinylist = [123, 'runoob']
print (list)            # 打印整个列表
print (list[0])         # 打印列表的第一个元素
print (list[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
print (list[2:])        # 打印列表从第三个元素开始到末尾
print (tinylist * 2)    # 打印tinylist列表两次
print (list + tinylist)  # 打印两个列表拼接在一起的结果
# 列表中元素的改变
list[0] = 'dcba'                # 将列表list中的第一项修改为'dcba',若在'dcba'外加中括号，将会变成列表嵌套，第一项会被替换为['dcba']
list[3:] = ['wjj',3.14,926]     # 将列表list中第四项到末尾的项替换为'wjj',3.14,926
list[1:3] = [789]               # 将列表list的第二项到第四项（不含第四项）替换为789，若不加中括号会出现TypeError: must assign iterable to extended slice
print(list)
# list[-3] = [24,35]              # 这样子写会将列表list的倒数第三项替换为一个列表[24,35]（即发生列表嵌套）而不是替换为两个元素
list = list[:-3] + [24,35] + list[-2:] # 完成元素替换的正确写法
print(list)
# 步长为负数的应用：翻转字符串
def reverseWords(string): 
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = string.split(" ") 
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],  
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1] 
    # 重新组合字符串
    output = ' '.join(inputWords) 
    return output
if __name__ == "__main__": 
    string = 'I like runoob'
    rw = reverseWords(string) 
    print(rw)

# 元组
# 元组与列表类似，但是元组是不可更改的
# 元组在Python中写在小括号里，元素之间用逗号隔开
# 元组支持所有列表的操作，只是不支持修改元素
# 字符串可以被看作一种特殊的元组，但是isinstance(str,tuple)会返回False
# 可以使用tup1 = ()来创建空元组
# 若想要创建只有一个元素的元组，应当这样写：tup2 = (content1,)，若直接写成tup2 = (content1)，Python会将content1直接视作一个元素，而不是创建包含content1的元组

# 集合
# Python中的集合与数学中的集合类似，是一种无序、可变的数据类型，用于储存唯一的元素
# 集合中的元素不会重复，若创建时或添加元素后存在重复的元素，Python只会保留其中的一个
# 在Python中，集合用{}创建，中间的元素用逗号隔开
# 集合中的元素必须是不可变数据类型
# 集合的示例：
{'string',123,3.14,3+4j}
# 另外，也可以使用set()来创建集合
# 需要注意的是，空集合必须使用set()来创建，使用{}创建的是空字典
# set()函数中若只填一个字符串，创建出的集合的元素将由该字符串中单个的字符组成，而不是以字符串为元素
# 示例：
sites = {'Google', 'Taobao', 'Bilibili', 'Facebook', 'Zhihu', 'Baidu', "Google"}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Bilibili' in sites :
    print('Bilibili 在集合中')
else :
    print('Bilibili 不在集合中')
if 'wjj' in sites :
    print('wjj 在集合中')
else :
    print('wjj 不在集合中')
# 集合的运算：
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

# 字典
# 字典是一种无序、可修改的数据类型，是一种映射类型
# 字典用 { } 标识，它是由无序的键(key) : 值(value)组成的
# 字典的键必须使用不可变数据类型，且在同一个字典中，键（key）必须是唯一的
# 示例：
dict = {}                 # 创建空字典
dict['one'] = "教程"       # 向字典中添加键为'one'，值为"教程"的元素
dict[2]     = "工具"       # 向字典中添加键为2，值为"工具"的元素
tinydict = {'name': 'wjj','code':1, 'site': 'https://www.github.com/wjj-8283'}
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

# 字节数组（bytes）类型（不常用）
# 在Python中，bytes类型表示的是不可变的二进制序列。
# 与字符串类型不同的是，bytes类型中的元素是整数值（0到255之间的整数），而不是Unicode字符。
# bytes类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。在网络编程中，也经常使用bytes类型来传输二进制数据。
# 创建bytes对象的方式有多种，最常见的方式是使用b前缀：
# 此外，也可以使用bytes()函数将其他类型的对象转换为bytes类型。bytes()函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：
# x = bytes("hello",encoding="utf-8")
# 与字符串类型类似，bytes类型也支持许多操作和方法，如切片、拼接、查找、替换等等。同时，由于bytes类型是不可变的，因此在进行修改操作时需要创建一个新的bytes对象。
# 例如：
x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
# 需要注意的是，bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值。
# 例如：
x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")
# 其中ord()函数用于将字符转换为相应的整数值。