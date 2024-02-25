# open(name, mode)  name: strings or files directory  mode: r, w, a
"""
# 读取及修改模式
# w
file = open('myfile.txt', 'w')
file.write('Welcome to check my file')
file.close()
# r
file = open('myfile.txt', 'r')  # same as file = open('myfile.txt)
file.close()
# a
file = open('myfile.txt', 'a')
file.write('\nAppend a txt file')
file.close()

file = open('file.txt','w')
file.write('This is test file')
file.close()
"""
"""
# file.read()     读取文件
file = open('a_test_file', 'r')
print(file.read())  # print(file.read(20))会读取20个字节
file.close()
# file.readlines     以行的方式读取，返回值为list
file = open('a_test_file')
line_content = file.readlines()  # print(file.readlines(20))依然是读取20个字节
print(line_content)
file.close()
# file.readline     一次读取一行内容
file = open('a_test_file')
for i in range(4):
    line_content1 = file.readline()
    print(line_content1, end='')
file.close()
"""
"""
# r, rb, r+, rb+  文件指针位置在开头，读取模式
# w, wb, w+, wb+  文件指针位置在开头，覆盖原数据
# a, ab, a+, ab+  文件指针位置在结尾
# 加b为二进制格式，加+可读可写
file = open('file.txt', 'r+')
print(file.read())

file.close()
"""
"""
# 移动文件指针 file.seek(偏移量， 起始位置)
# 0: 文件开头  1: 当前位置  2: 末尾位置
file = open('a_test_file', 'a+')
file.seek(0)  # 将指针位置移动到最开头
print(file.read())

file.close()
"""
"""
# file backup
old_name = 'sound.txt.mp3'
index = old_name.rfind('.')
if index > 0:
    file_name = old_name[:index]
    file_postfix = old_name[index:]
    new_name = file_name + '_copy' + file_postfix
    # create the old file
old_file = open(old_name, 'w')
for i in range(10):
    old_file.write(str(i) * 5)
    old_file.write('\n')
old_file.close()
# writing data into backup file
old_file = open(old_name, 'rb')
new_file = open(new_name, 'wb')
# 由于不确定文件大小，可以使用循环读取文件写入，直到文件数据结束终止循环
while True:
    content = old_file.read()
    if len(content) == 0:
        break
    new_file.write(content)
old_file.close()
new_file.close()
"""
"""
# files and folders operation, import os database first
# os.rename    os.remove
import os
# create a file
file = open('file.txt', 'w')
file.close()
# rename this file
os.rename('file.txt', 'file_rename.txt')  # rename 也可以重命名directory
# remove this file
os.remove('file_rename.txt')
# create and remove a folder
os.mkdir('folder1')
os.rmdir('folder1')
# get the current directory
src = os.getcwd()
print(src)
# change current working directory
os.chdir('folder_test')
# list all the files in current working directory
print(os.listdir())
"""
"""
# 批量修改文件名，既可以添加指定字符串，又能删除字符串
import os

file_list = os.listdir()
print(file_list)
# 谨慎运行
flag = 1
for i in file_list:
    if flag == 1:
        new_name = 'Python_' + i
    elif flag == 2:
        num = len('Python_')
        new_name = i[num:]
    os.rename(i, new_name)
"""
