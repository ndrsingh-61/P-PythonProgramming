import random

comp_turn = random.randint(0, 2)
if comp_turn == 0:
    computer = 'rock'
elif comp_turn == 1:
    computer = 'paper'
else:
    computer = 'scissors'

user_turn = input("choose rock, paper, scissors")
if user_turn == 'rock' and computer == 'paper':
    print("computer won")
elif user_turn == 'rock' and computer == 'scissors':
    print("user won")
elif user_turn == 'paper' and computer == 'rock':
    print("user won")
elif user_turn == 'scissors' and computer == 'paper':
    print("user won")
elif user_turn == 'paper' and computer == 'scissors':
    print('computer won')
else:
    print('computer won')
