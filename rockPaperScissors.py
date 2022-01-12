import random


computer_choice = random.choice(['scissors', 'rock', 'paper'])

user_choice = input('Do you want - rock, paper, or scissors? \n')
win = 'You Won! ' + user_choice + ' beats ' + computer_choice

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(win)
elif user_choice == 'paper' and computer_choice == 'rock':
    print(win)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(win)
else:
    print('You lose :( the computer chose ' + computer_choice)
