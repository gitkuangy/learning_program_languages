# + merge * multiply   # only works for strings, lists, tuple
# in and not in   # works for strings, lists, tuple and Dictionary
# len() del/del() max() min() range(start, end, step) enumerate()
# data conversion: list() tuple() set()

str1 = 'abcdef'
str2 = 'ghijkl'
list1 = [1, 2, 3, 3, 5, 6]
list2 = ['e', '6', 'r']
tuple1 = (1, 3, 2)
tuple2 = ('w', 3, 6)
dic1 = {'key1': 'value1', 'key2': 'value2'}
dic2 = {'key3': 'value3', 'key4': 'value4'}
set1 = {'u', 5, 8, 3}
"""
# +: merge
print(tuple2 + tuple1)
# *: multiply
print(str1 * 3)
print(list1 * 3)
print(tuple2 * 3)
# in and not in
print('value1' in dic1)
print('value3' in dic2.values())
"""
"""
# len()  del/del()  max() min()
del str1
del list1[0]
print(list1)
del(dic1['key1'])
print(dic1)
print(max(list2))
"""
"""
# range
for i in range(0, 10, 2):
    print(i, end=' ')
# enumerate: 返回值为tuple， 第一个数据为下标，第二个数据为原对象里的数据
for a in enumerate(list1, start=0):
    print(a)
"""
"""
# data conversion: tuple(), list(), set()
print(tuple(list1))
print(list(tuple1))
print(set(list1))
"""

