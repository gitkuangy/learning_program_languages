import random

time = 3
print('<<<<<< GAME STARTS! >>>>>>')
while time > 0:
    guess = input('Big or Small? : ')
    point_1 = random.randrange(1, 7)
    point_2 = random.randrange(1, 7)
    point_3 = random.randrange(1, 7)
    a_list = [point_1, point_2, point_3]
    random_sum = sum(a_list)
    print('<<<<<< Roll the Dice >>>>>>')
    print('The points are [', point_1, point_2, point_3, ']')
    if 11 <= random_sum <= 18:
        if guess == 'Big':
            print('You win!')
        else:
            print('You lose!')
    else:
        if guess == 'Small':
            print('You win!')
        else:
            print('You lose!')
    time = time - 1
print('Game over!')
