# define, call function
"""
# define a function and list its documentation
def add_num(a, b):
#   此处用三引号加入函数的说明文档
    return a + b

# 说明文档，在函数内第一行位置加上自己的函数说明，此处help内只需输入函数名，不要调用函数
help(add_num)
"""

# print lines  使用嵌套函数
"""
def print_line():
    print('-' * 10)

def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(4)
"""
"""
def sum_num(a, b, c):
    return a + b + c


def average(a, b, c):
    result = sum_num(a, b, c) / 3
    return result


print(average(8, 6, 10))
"""
"""
# 全局变量
a = 20
def test1():
    print(a-2)  # 全局变量


def test2():
    global a  # 申明为全局变量a
    a = 40   # 如果要在函数内修改全局变量，则使用： global a, 否则为局部变量
    print(a)
test1()
test2()
print(a)
"""
"""
# Multi-function execution procedure 针对全局变量
glo_num = 0


def test1():
    global glo_num
    glo_num = 100


def test2():

    print(glo_num)


test1()
test2()
"""

"""
def test1():
    return 1, 2   # 默认类型为tuple， 也可以直接返回 dictionary， list 等

print(test1())
print(type(test1()))
"""

"""
# function's parameter
def user_info(name, age, gender):
    print(f'Your name is {name}, age is {age}, gender is {gender}')


user_info('Jame', 30, 'Male')  # 位置参数
user_info(age=20, gender='Female', name='jin')  # 关键字参数, 不需要按照位置参数


# 缺省参数, 直接在函数定义时指定参数值
def user_info1(name, age, gender='male'):
    print(f'Your name is {name}, age is {age}, gender is {gender}')


user_info1('SKK', 80)


# 不定长参数, 组包
# 包裹位置传递
def user_info2(*args):  # args 接收所有的位置参数，合并为一个tuple
    print(args)


# 包裹关键字传递
def user_info3(**kwargs):  # kwargs 接收所有关键字参数， 合并为一个字典
    print(kwargs)


user_info2(9, 'k')
user_info3(name='jane', age=30, gender='Male')


# tuple 拆包
def return_num():
    return 20, 30


num1, num2 = return_num()
print(num1, num2)

# dictionary 拆包
dict1 = {'name': 'Jane', 'age': 34}
c, d = dict1
print(dict1[c], dict1[d])
"""
"""
# swap variables
a, b = 1, 2
a, b = b, a
print(a, b)
"""
"""
# id() 返回变量的地址
# 不可变类型数据 int, float, string, tuple
a = 2
b = a
print(id(a), id(b))
a = 1
print(b)   # 2, 不可变数据类型
print(id(a), id(b))
# 可变类型数据 list, Dictionary, Set
aa = [10, 20, 30]
bb = aa
print(id(aa), id(bb))
aa.append(40)  # 不需要为aa重新选择一个地址
print(bb)  # [10, 20, 30, 40]  可变数据类型
print(id(aa), id(bb))
"""
"""
# 实参的引用
def test1(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))


# 引用不可变数据
b = 11
test1(b)
# 引用可变数据
c = [11, 22]
test1(c)
"""



