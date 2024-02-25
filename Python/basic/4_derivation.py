# derivation: works only for lists, dictionary and set
"""
# lists derivation 列表推导式
list1 = []  # create an empty list
# use while loop
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)
# use for loop
for i in range(9, 0, -1):
    list1.append(i)
print(list1)
# use list derivation:   ********************************************************
list2 = [i for i in range(5)]  # use for in list
print(list2)
# create a list
list3 = [i for i in range(20) if i % 2 == 0]  # use for and if in list
print(list3)
# create a list with tuples in it
list4 = [(i, j) for i in range(6) if i % 2 == 0 for j in range(10) if j % 2 != 0]    # nested for loop
print(list4)
"""
"""
# dictionary derivation: 将列表合并为一个字典或提取字典中的目标数据
# create a dictionary
dict1 = {i: i * 2 for i in range(3)}
print(dict1)
# merge two lists into one dictionary
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'male', 7]
dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)
# Extract the target data in a dictionary
dict3 = {'MBP': 268, 'HP': 125, 'DELL': 201, 'LENOVO': 199, 'ACER': 99}
dict3_3 = {key: value for key, value in dict3.items() if value >= 200}
print(dict3_3)
list3 = [name for name in dict3.keys()]
print(list3)
"""
"""
# set derivation
list1 = [1, 1, 2]
# create a set whose elements are double of lists above
set1 = {i * 3 for i in list1}
print(set1)
"""
