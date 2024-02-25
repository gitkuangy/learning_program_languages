"""
# 1. Data type - 数据类型
# int, float, str
# bool
a = True  # /False
# list
b = [10, 20, 30]
# tuple
c = (10, 20, 30)
# set
d = {10, 20, 30}
# dict -- 字典，键值对
e = {'name': 'Tom', 'age': 30}
print(type(a), '\n',type(b), '\n',type(c), '\n',type(d), '\n',type(e))
"""

"""
# 2. formatting symbols - 格式化符号（用于格式化输出）
# % + s, d, f, c, u, o, x, X, e, E, g, G

age = 18  # int
name = 'Tom'  # string
weight = 93.2  # float
stu_num = 28  # int, 整数用三位数表示，如 28--028, %03d
print('I am now %d years old' % age)
print('My name is %s' % name)
print('My weight is %.2f lb' % weight)  # 保持两位小数
print('My student ID is %04d' % stu_num)  # int, 整数用四位数表示，如 28--0028
print('My name is %s, %d years old, student ID is %04d' % (name, age, stu_num))  # 混合输出
# 以上所有数据都可以用 %s 格式化为字符串
# 也可以用 f' { } ' 来格式化，且此方法更高效，用法如下
print(f'My name is {name}, and my age is {age}')
"""

"""
# 3. escape character and terminator 转义字符和print结束符
# \n enter
# \t tab #4个字节
print('Hello\n\tworld')
# print(  , end = '\n') #\n 为print的默认结束符，可把\n 更换为其他任意符号作为结束符号，如下
print('Hello', end='.......')
print('World')
"""
"""
# 4. data type conversion
# int(), float(), str(), eval(), tuple(), list()
# complex(real [,imag]), epr(), chr(), ord(), hex()
# eval() 可以将字符串中的数据转化为数据本身类型
# input() 读取的数据最后结束类型都为字符串
"""

"""
# 5. operator 运算符
# arithmetic: +,-,*,/,//，%，**，（）
# assignment: =  # single/multiple variable(s) assignment
num1, float1, str1 = 1, 1.2, 'hello',
print(str1)
print(num1, float1)
# compound assignment: +=, -=, *=, /=, //=, %=, **= 次于计算运算符 ex. a+=c means: a = a+c
# c += a+b 先计算 a+b 再计算+=
# compare: ==, !=, >, <, >=, <=
# logic: and, or, not
# a and b and c # 只要有一个值为0， 结果为0， 否则结果为最后一个非0数字
# a or b or c  # 只有所有值为0 才返回0， 否则结果为第一个非0数字
"""
"""
# 6. conditional statements 条件语句  if: else   if: elif: else
# 经典猜拳游戏 见rock_paper_scissors项目
# ternary expression 三元表达式： 条件成立执行表达式 if 条件 else 条件不成立表达式
# 三元表达式可用于取大小值，如：
a = 2
b = 4
c = a if a > b else b      *****************************************************************
print(c)

aa = 10
bb = 15
cc = aa - bb if aa > bb else bb - aa      *****************************************************************
print(cc)
"""
"""
# 7. Loops: while and for
i = 0
while i <= 2:
    print(f'count {i}')
    i += 1

# break: 退出整个循环  continue: 退出当前循环继而执行下一次循环
i = 1
while i <= 5:
    if i == 3:
        i += 1  # 如果要使用 continue 必须加这一步
        continue  # break 退出此循环, 去掉上一步 i += 1
    print(f'you ate {i} apple')
    i += 1

# while nested
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f'excuted {i}{j} times')
        j += 1
    i += 1
"""
"""
# LOOPS: for i in str1.  break and continue
str1 = 'kuangy'
for i in str1:
    if i == 'n':
        break  # continue
    print(i)
"""
"""
# while...else...  while 循环正常结束之后才能执行 else 之后的代码 
# for...else...  for 循环正常结束之后才能执行 else 之后的代码 
i = 1
while i <= 3:
    if i == 2:
        i += 1
        continue  # 用break去掉以上条件， 
    print(f'**{i}**')
    i += 1
else:
    print('finished')
"""

"""
# 8. string single/double/triple quotes '...' "..." '''...''' """ """ 三引号支持换行，且内里可以再用引号
# 单引号前面加一个转义符号, 可以输出单引号 '
a = '''I'm 
kuangying'''
print(a)
"""
"""
# string subscript str[2] and slice  str [2:5:1] 起始：结束：步长
# 下标 -1 表示最后一个数字 如 str[-1]
str1 = '012345678'
print(str1[2:6:2])
print(str1[:4])
print(str1[4:])
print(str1[::-1])
"""
"""
# strings common operation methods: 查找， 修改， 判断
# 字符串是不可变的数据类型
# a. 查找: find/index/count('子串', 开始位置下标， 结束位置下标)
# find() 检测某个子串是否被包涵在这个字符串中，找到返回位置下标，否则返回-1， rfind()从右侧开始检测
# index()  检测某个子串是否被包涵在这个字符串中，找到返回位置下标，否则报错  rindex()从右侧开始查找
# count()  检测某个子串在此字符串中出现的次数
mystr = 'you and me and she are friends'
print(mystr.find('a'))  # find('a', 2, 10) 2和10分别为要选择的起始结束下标
print(mystr.count('a'))
# b. 修改:
# replace(旧子串，新子串，替换次数) 返回值为新的字符串
# split(分割字符，分割字符出现次数) 返回值类型为列表
# join(多个字符串组成的列表) 合并多个字符串, 括号内操作对象为list, list包含几个strings，返回对象为一个string
# mystr.capitalize() 将字符串中第一个字符转化为大写，其他全部化为小写
# mystr.title() 将字符串中每个单词首字母转换成大写
# mystr.upper() 将字符串中的小写转大写
# mystr.lower() 将字符串中的大写转小写
# mystr.lstrip() mystr.rstrip() mystr.strio() 删除字符串左/右/两侧侧空白字符
# mystr.ljust(字符总长度，填充字符) mystr.rjust(字符总长度，填充字符) mystr.cneter(字符总长度，填充字符) 左/右/居中对齐，空白处可使用字符填充
print(mystr.replace('me', 'her'))
print(mystr)
newstr = mystr.split(' ')
print(newstr)
print(type(newstr))
# join的使用如下：
mylist = ['aa', 'bb', 'cc']
newstr1 = '...'.join(mylist)
print(newstr1)
# c. 判断：返回 True or False
#  mystr.startswith(子串，开始下标，结束下标） mystr.endswith(子串，开始下标，结束下标） 判断是否以某子串开始/结尾
#  mystr.isalph()  mystr.isdigit()  mystr.alnum()  mystr.isspace()判断非空且是否都为字母/数字/字母或数字/空格
"""
a = '23j'
b = 'ijnn'
mystr = '     yOu and me And she are friends    '
str1 = mystr.ljust(100, 'h')
print(str1)
