"""
# 3 + 2 + 1 use recursion
def sum_num(num):
    if num == 1:
        return 1
    return num + sum_num(num - 1)


print(sum_num(3))
"""

"""
# lambda expression
# function has one return value and one expression, ex:
def fun1():
    return 1


result = fun1()
print(result)

fun2 = lambda: 100  # fun2 is a function name, lambda is a function
print(fun2)  # lambda's memory address
print(fun2())  # call this function return its return value
"""

"""
# use def to calculate a+b
def add_num(a, b):
    return a + b


result = add_num(2, 3)
print(result)

# use lambda to calculate a+b 
fun1 = lambda a, b: a + b
print(fun1(3, 4))
"""
"""
# lambda expressions:
fun1 = lambda: 100  # no parameter
print(fun1())
fun2 = lambda a: a  # one or more parameters
print(fun2('hello world'))
fun3 = lambda a, b, c=20: a + b * c  # default parameters
print(fun3(10, 2))
fun4 = lambda *args: args  # variable parameter * args, return a tuple
print(fun4(10, 20, 30))
fun5 = lambda **kwargs: kwargs  # variable parameter **kwargs, return a dictionary
print(fun5(name='Python', age='40'))
"""
"""
# lambda practical applications
# find the bigger value
fun1 = lambda a, b: a if a > b else b
print(fun1(20, 30))
# sort list by dictionary keywords
students = [
    {'id': 1, 'name': 'Joe', 'gender': 'Male', 'grade': 98.0},
    {'id': 2, 'name': 'James', 'gender': 'Male', 'grade': 90.0},
    {'id': 3, 'name': 'Jane', 'gender': 'Female', 'grade': 99.5},
    {'id': 4, 'name': 'Tom', 'gender': 'Male', 'grade': 95.1}
]
students.sort(key=lambda i: i['name'])
print(students)
"""
