# high order function: pass a function as an argument of another function
"""
# abs() return absolute value
# round() rounding a number
# 两个数取绝对值后再求和，以下两种方法：
# 1. 固定为绝对值的方法：
def add_num1(a, b):
    return abs(a) + abs(b)  # 如果想求四舍五入值的和，那么可以把abs换成round，那么就可以把函数作为参数传入


result1 = add_num1(4, -3)
print(result1)


# 2. 函数作为参数的方法：
def add_num2(a, b, fun):
    return fun(a) + fun(b)


result2 = add_num2(-4, 5, abs)
print(result2)
result3 = add_num2(-4.8, 5.2, round)
print(result3)
"""
# 几种高阶函数的应用： map(), functools.reduce(), filter()
"""
# 1.
# map(function,list) 将函数作用到list中的每个元素，但此处返回的是一个map的迭代器地址
list1 = [1, 2, 3, 4, 5]


def power2(x):
    return x ** 2


result_add = map(power2, list1)  # 返回的是一个地址

print(result_add)
print(list(result_add))  # 将地址转化为list, 也可以转化为set， tuple
"""
"""
# 2.
# functools.reduce(function, list)  每次function计算的结果继续和list的下一个元素做累积计算
# reduce 需要在functools库里调用
# 此处 function 必须接收2个参数
# 例，计算list中各个数字的累加和：
import functools  # 一般 import 某个库放在文件顶端

list1 = [1, 2, 3, 4, 5]


def add_num(a, b):
    return a + b


result = functools.reduce(add_num, list1)
print(result)
"""
"""
# 3.
# filter(function, list) 用于过滤序列，过滤掉不符合function的数据(过滤掉false值)，返回值为地址
list1 = [1, 2, 3, 4.8, 5, 6.2, 7, 8]


def even_num(x):
    return x % 2 == 0


result = filter(even_num, list1)
print(result)
print(list(result))
"""