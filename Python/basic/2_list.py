# 1. LIST and its common uses
name_list = ['Tom', 'Lily', 'Rose', 'Lily']
num_list = [0, 4, 3, 6, 4, 5, 9, 2, 8]
"""
# 查找： list.index('Tom')  list.count('Tom')  list.len(list)
print(name_list.index('Lily'))
print(name_list.count('Lily'))
# 判断: in     not in
print('Tom' in name_list)
print('Tom' not in name_list)
# exercise: Determine if an account exists in a list
name = input('Input your username: ')
while name in name_list:
    print('This name has been used, try another one!')
    name = input('Input your username: ')
else:
    print(f'You have created a new account: {name}')
"""

# 添加: list.append('str')  list.extend('list')  list.insert(位置下标，插入数据)
# list.append('a') 在末尾增加一个数据a, 这个数据 a 可以是列表，字符串
# list.extend('a') a如果为列表，将被拆分为列表里的字符串，如果为字符串，则被拆分为单个字符
# 列表数据可更改
"""
name_list.append('Kany')
print(name_list)
name_list.append(['Jerry','Jason'])
print(name_list)
name_list.extend(['Jerry','Jason'])
print(name_list)
name_list.extend('YYY')
print(name_list)
name_list.insert(2,'KKK')
print(name_list)
"""
"""
# 删除:
# del list or del list[2]
del name_list[1]
print(name_list)
# list.pop() 弹出并返回最后一个数据，如果加上数字则弹出返回相应位置数据
name = name_list.pop()
print(name)
print(name_list)
# list.remove(数据) 移除某个数据, 返回值为none
name_list.remove('Tom')
print(name_list)
# list.clear() 清空列表
name_list.clear()
print(name_list)
del name_list
print(name_list)
"""
"""
# 修改: list[2] = ' ', list.reverse(), list.sort(key: none, reverse = False) False 为升序排列，True 为降序排列
num_list[8] = 9
print(num_list)
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)
num_list.sort(reverse = True)
print(num_list)
"""
"""
# 复制： list.copy() 返回值为列表
num2_list = num_list.copy()
print(num2_list)
"""
"""
# list loops traversal 列表的循环遍历
# 用 while 依次打印列表中各个数据
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
# 用 for 依次答应列表中各个数据, 遍历
for name in name_list:
    print(name)
"""
# nested lists 列表嵌套
nest_namelist = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
print(nest_namelist[1][0])
