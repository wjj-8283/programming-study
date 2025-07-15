# Python基本数据类型有6个，分别为数字（numbers）、字符串（string）、布尔类型（bool）、列表（list）、元组（tuple）、集合（set）、字典（dictionary）
# 其中可变的数据类型有：列表、集合、字典，
# 不可变数据类型有：数字、字符串、元组

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
# 其中start为切片开始的索引，end为切片结束的索引（不含该字符），sep为步长
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
# 列表的示例：
["string",12,12.0,True,["new_list",120,60]]
# 示例程序：
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]  # 定义一个列表
tinylist = [123, 'runoob']

print (list)            # 打印整个列表
print (list[0])         # 打印列表的第一个元素
print (list[1:3])       # 打印列表第二到第四个元素（不包含第四个元素）
print (list[2:])        # 打印列表从第三个元素开始到末尾
print (tinylist * 2)    # 打印tinylist列表两次
print (list + tinylist)  # 打印两个列表拼接在一起的结果
