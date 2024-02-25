# project: Create a student operating system
# create a empty student list which will including: id, name, gender, grade

mem_list = [
    {'id': 1, 'name': 'Joe', 'gender': 'Male', 'grade': 98.0},
    {'id': 2, 'name': 'James', 'gender': 'Male', 'grade': 90.0},
    {'id': 3, 'name': 'Jane', 'gender': 'Female', 'grade': 99.5},
    {'id': 4, 'name': 'Tom', 'gender': 'Male', 'grade': 95.1}
]


# create a function shows users' interface
def option():
    print('Please choose these options below:\n'
          '\t1. Add a membership\n'
          '\t2. Delete a membership\n'
          '\t3. Modify a membership\n'
          '\t4. Search a membership\n'
          '\t5. Display all members\n'
          '\t6. Exit')
    print('-' * 20)


# function 1: add a member
def add_mem():
    global mem_list
    # user input a member information:
    mem_id = int(input("Please input an id of the student: "))
    # check if this id has exist in the system
    for i in mem_list:
        if mem_id == i['id']:
            return
    name = input("Please input the member's name you want to add: ")
    gender = input(f"Please input {name}'s age: ")
    grade = float(input(f"Please input {name}'s grade: "))
    # if id is new, then create a new dictionary to store the student's info
    mem_info = {'id': mem_id, 'name': name, 'gender': gender, 'grade': grade}

    # add this student into students' list
    mem_list.append(mem_info)
    print(mem_list)
    user_choice = input("Do you want to add another student? Input 'y' or 'n'.")
    if user_choice == 'y':
        add_mem()
    else:
        return


# function 2: delete a member
def del_mem():
    global mem_list
    # user input a student to be deleted
    del_id = int(input("Enter the id of the student you want to delete: "))
    # check if the student exists in the list
    for i in mem_list:
        if del_id == i['id']:
            mem_list.remove(i)
            break
    else:
        print('This student does not exist.')
    print(mem_list)


# function 3: modify a member's info
def modify_mem():
    global mem_list
    # user input a student to be modified
    modify_id = int(input("Enter the id of the student you want to modify: "))
    # check if the student exists in the list
    for i in mem_list:
        if modify_id == i['id']:
            i['name'] = input(f"Please input {modify_id}'s new name: ")
            i['gender'] = input(f"Please input {modify_id}'s age: ")
            i['grade'] = float(input(f"Please input {modify_id}'s grade: "))
            break
    else:
        print('This student does not exist.')
    print(mem_list)


# function 4: search an existed member
def search_mem():
    global mem_list
    search_id = int(input("Please input the student's id you want to search: "))
    for i in mem_list:
        if search_id == i['id']:
            print('The member you want to search is: ')
            print(i)
            break
    else:
        print('The student you are searching does not exist.')


# function 5: display all members
def dis_mem():
    global mem_list
    print('student id\tstudent name\tstudent gender\tstudent grade')
    for i in mem_list:
        print(f"{i['id']}\t\t{i['name']}\t\t{i['gender']}\t\t{i['grade']}")


# function let users to choose which one he wants to enter
def mem_fun(n):
    if n == 1:
        add_mem()
    elif n == 2:
        del_mem()
    elif n == 3:
        modify_mem()
    elif n == 4:
        search_mem()
    elif n == 5:
        dis_mem()
    elif n == 6:
        print('Exit the system successfully')
        return


# main function
option()
user_choose = int(input('Your choice is: '))
while user_choose != 6:
    if user_choose > 6 or user_choose < 1:
        print('Wrong input!')
        user_choose = int(input('Please enter a choice between 1-6: '))
    else:
        mem_fun(user_choose)
        option()
        user_choose = int(input('Your choice is: '))

print('Exit the system successfully')
