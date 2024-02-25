import random

print("------Welcome to play the 'rock, paper and scissors' game------")
number = int(input('How many times do you want to play this game? '))
count = number
while count > 0:
    player = int(input('Please choose below numbers representing a gesture: '
                       '(0 - rock; 1 - paper; 2 - scissors)\n'))
    computer = random.randint(0, 2)
    if player == 0:
        print('Yours is rock')
    elif player == 1:
        print('Yours is paper')
    elif player == 2:
        print('Yours is scissors')
    else:
        print('wrong input')
    if computer == 0:
        print('Mine is rock')
    elif computer == 1:
        print('Mine is paper')
    elif computer == 2:
        print('Mine is scissors')

    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print('You win!')
    elif player == computer:
        print('Draw!')
    else:
        print('I win!')

    count -= 1
