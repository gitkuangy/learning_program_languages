# tuple data cannot be modified
# multiple and single tuple： mul_tuple = (1,2,3)  single_tuple = (1,)
t1 = ('a', 'b', 'c', 'd')  # 下标 t1[0]
# 查找： t1.index() t1.count() len()
# 修改： 不能用下标修改， 但内含列表可以修改
t2 = ('a', 'b', ['c', 'e'], 'd')  # t2[2] 可以修改

# Dictionary 如果一个对象有多个属性可以使用字典，用key: value表示
dict1 = {'name': 'Tom', 'age': '20', 'gender': 'male'}
dict3 = {} # 创建空字典
dict2 = dict()  # 创建空字典
"""
# 修改新增数据
dict1['name'] = 'Jane'
dict1['ID'] = 55555
print(dict1)
print(type(dict1['ID']))
"""
# 删除，清空字典： del() clear()   del(dict1['name']]  dict1.clear()
# 几个常用函数 get() keys() values() items()
"""
# get 只是返回一个对象，并不会给字典增加数据
print(dict1.get('name'))
print(dict1.get('Job', 'teacher'))
print(dict1.get('Job'))
"""
"""
print(dict1.keys())
print(dict1.values())
print(dict1.items())
"""
"""
# 字典的循环遍历 key， value，item, key&value
for a in dict1.keys():
    print(a, end=' ')
print()
for value in dict1.values():
    print(value, end=' ')
print()
for item in dict1.items():
    print(item)
for key, value in dict1.items():
    print(f'{key}: {value}')
"""
"""
# set 集合的创建
s1 = {1, 1, 2, 3, 4, 3, 5}
s2 = set('1234567')
s3 = set()
# 增加数据: add()增加单一数据， update()增加序列数据
s3.add(233)
s3.update([27, 68, 25, "m"])
print(s3)
# 删除数据： remove() discard() pop()
s2.remove('3')  # 使用discard的话，如果要删除的数据不存在，不会报错
print(s2)
del_num = s2.pop()  # 随机删除一个数据
print(del_num)
print(s2)
# 数据查找： in   not in
print(1 in s2)
"""
