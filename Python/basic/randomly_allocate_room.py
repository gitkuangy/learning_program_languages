# put 8 students into 3 classrooms randomly, hint: use nested list and for loop
import random

students = ['A', 'B', 'C', 'D', 'E', 'F', 'E', 'H']
classroom = [[], [], []]
for name in students:
    random_num = random.randint(0, 2)
    classroom[random_num].append(name)
print(classroom)
i = 1
for room in classroom:
    print(f'class room {i} has {len(room)} students: ', end='')
    for name in room:
        print(name, end=' ')
    print()
    i += 1
