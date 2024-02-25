"""
# calculate trapezoid's area
def trapezoid_area(base_up, base_down, height):
    result = (base_up + base_down) * height / 2
    return result
print(trapezoid_area(3, 2, 1))

# print default parameter 'sep' is space, below changed it into enter
print('*', '**', '***', sep='\n')

# modify file and its content
def file_change(name, message):
    half_path = '/Users/kuangying/Documents/python/py0/'
    full_path = half_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(message)
    file.close()
    print('Done')
file_change('file', 'changed successfully')"""

"""
# input a password and check if it is right
def account_login():
    password = input('Enter a password: ')
    if password == '123456':
        print('Right guess')
    else:
        print('wrong password')
        account_login()
account_login()"""

"""
#enter and reset password
password_list = ['*#*#', '123456']


def password_change(new1, new2):
    if new1 == new2:
        return new1
    else:
        print('Password does not match')
        new1 = input('Please enter a new password: ')
        new2 = input('Please enter the new password again: ')
        password_change(new1, new2)


def account_login():
    password = input('Please enter password: ')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Correct input, login seccessfully!')
    elif password_reset:
        new1 = input('Please enter a new password: ')
        new2 = input('Please enter the new password again: ')
        new_password = password_change(new1, new2)
        password_list.append(new_password)
        print('Your password has been changed successfully')
    else:
        print('Wrong input')
        account_login()


account_login()"""
"""
# for loop
num = 6
for num in range(1, 11):
    print(str(num) + ' + 1 = ', (num + 1))
print(num)
"""
"""
# for loop and if 
songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print(song, '-Dio')
    elif song == 'Thunderstruck':
        print(song, '-AC/DC')
    elif song == 'Rebel Rebel':
        print(song, '-David Bowie')
    else:
        print('None')"""

"""
# exercise 1: Create 10 txt files
file_numbers = 1
while file_numbers < 11:
    half_path = '/Users/kuangying/Documents/python/py0/'
    full_path = half_path + str(file_numbers) + '.txt'
    file = open(full_path, 'w')
    file.write(str(file_numbers))
    file.close()
    file_numbers = file_numbers + 1
"""

"""
# exercise 2: Fail to try to calculate a compounded interest
# int and str problem
def invest(amount1, rate1, time1):
    for year in range(1, time1):
        new_amount = amount1 + amount * rate1 / 100
        print('year ' + str(year) + ': ' + '$' + str(new_amount))


amount = input('Enter your principal amount: ')
rate = input('Enter your rate without the %: ')
time = int(input('Enter the years you keep money in: '))
invest(amount, rate, time)
"""

"""
# print even numbers in 1~100
for even_num in range(1, 101):
    if even_num % 2 == 0:
        print(even_num)
#list
fruit = ['pineapple', 'pear']
#fruit.insert(1,'grape')
print(fruit)
"""
