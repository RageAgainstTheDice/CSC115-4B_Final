import random
import time

'''
if user_choice == comp_choice:
    print('tie')
elif user_choice == 1 and comp_choice == 3:
    Print('win')
'''


def rock_paper_scissors():
    user_options = ['rock', 'paper', 'scissors']
    while True:
        user_choice = str(input('\nChoose between "rock," "paper," or "scissors" to use against the computer: '))
        comp_choice = random.randrange(1, 4)
        while user_choice not in user_options:
            print('Your input must be either "rock," "paper," or "scissors." Please try again.')
            user_choice = str(input())
        else:
            if user_choice == 'rock':
                num_choice = 1
            elif user_choice == 'paper':
                num_choice = 2
            else:
                num_choice = 3
            time.sleep(0.375)
            if comp_choice == 1:
                print('The computer has chosen "rock."')
            elif comp_choice == 2:
                print('The computer has chosen "paper."')
            else:
                print('The computer has chosen "scissors."')
            if comp_choice == num_choice:
                print('It\'s a tie! You must play again until one side wins.')
                continue
            elif num_choice == 1 and comp_choice == 3:
                print('You win!')
                break
            elif num_choice == 2 and comp_choice == 1:
                print('You win!')
                break
            elif num_choice == 3 and comp_choice == 2:
                print('You win!')
                break
            else:
                print('You lose!')
                break

rock_paper_scissors()
