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
print()
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
