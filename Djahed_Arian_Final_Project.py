import random
# I import the random module for use in the "lotto_num_generator" and "rock_paper_scissors" modules.


def display_project_info():
    print('\nName: Arian Djahed\nEmail: axd1587@miami.edu\nCourse: CSC115-4B (Python Programming for '
          'Everyone)\nMajor: Computer Science\nThis is the final project for CSC115-4B, or "Python Programming for '
          'Everyone.\nIt is a simple text-based program that gives the user different options to display different '
          'results with varying degrees of interactivity.')
    # Here, I define the first function, which simply prints the displayed information; I implemented \n so that I
    # wouldn't have to use multiple print statements.


def lotto_num_generator():
    lotto_list = []
    # First, I made an empty list so that things could be appended to it later down the line.
    for i in range(5):
        new_num = random.randrange(1, 70)
        while new_num in lotto_list:
            new_num = random.randrange(1, 70)
        lotto_list.append(new_num)
    # This for loop appends the first five values to the list; the nested while loop ensures no two number is the same.
    lotto_list.sort()
    lotto_list.append(random.randrange(1, 27))
    # I then sort the elements from smallest to largest and then append the final element, which must be done
    # separately because the range from which it is chosen is different.
    red_powerball = lotto_list.pop()
    print('\nToday\'s lottery numbers are: ')
    for i in lotto_list:
        print(i, end=' ')
    print(f'ball {red_powerball}')
    # I then print the results out, using a for loop to allow each element to print one at a time, with the exception
    # of the final element, which is popped out prior so that it can be printed after a keyword that denotes that it
    # is special amongst the numbers.


def pig_latin():
    input_str = str(input('\nEnter something to be converted into pig latin (no punctuation): '))
    str_list = input_str.split()
    new_list = []
    # First, I convert the input into a list with each word as its own element, and then create an empty list to
    # append the pig-latinised words into later.
    for i in str_list:
        new_word = i[1:] + i[0] + 'ay'
        new_list.append(new_word)
    # This for loop then pig-latinises each word one-by-one, combining (in order) all letters of the word except the
    # first letter, the first letter, and the "ay" part.
    for i in new_list:
        print(i, end=' ')
    print()
    # The for loop then allows for each now-pig-latinised word to be printed in order, separated by a space.


def rock_paper_scissors():
    user_options = ['rock', 'paper', 'scissors']
    # I made a list of valid inputs to later check with a while loop.
    while True:
        # Nesting everything in a "while True" loop allows me to control when I can exit the loop, which I shall do
        # with "break."
        user_choice = str(input('\nChoose between "rock," "paper," or "scissors" to use against the computer: '))
        comp_choice = random.randrange(1, 4)
        while user_choice not in user_options:
            print('Your input must be either "rock," "paper," or "scissors." Please try again.')
            user_choice = str(input())
        # This is where the user and computer choices are determined and where the system checks that the user input
        # is valid before continuing.
        else:
            if user_choice == 'rock':
                num_choice = 1
            elif user_choice == 'paper':
                num_choice = 2
            else:
                num_choice = 3
            # I assign each possible valid user choice with a number to make it easier to compare to the computer's
            # choice.
            if comp_choice == 1:
                print('The computer has chosen "rock."')
            elif comp_choice == 2:
                print('The computer has chosen "paper."')
            else:
                print('The computer has chosen "scissors."')
            # This part simply serves to let the user know the computer's choice.
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
            # Here, the actual choices of the computer and user are compared to produce the proper effect. Notice how
            # there is a "break" if there is a win or loss but a "continue" if there is a tie: this ensures that,
            # in the event of a tie, the game can keep going until somebody wins.


if __name__ == '__main__':
    # Putting the rest of the code in this conditional statement ensures that only this part is displayed should the
    # module be imported to another file.
    menu = int(input('Choose from the following options:\n1. Display Project Information\n2. Lottery Number '
                     'Generator\n3. Pig Latin\n4. Rock, Paper, Scissors\nPlease enter a number from 1 to 4 to execute '
                     'the command corresponding to said number.\n'))
    # Here, the options are given for the user to choose.
    while menu < 1 or menu > 4:
        print('The input must be a number between 1 and 4. Please try again.')
        menu = int(input())
    # This while loop ensures the user's input is valid.
    else:
        if menu == 1:
            display_project_info()
        elif menu == 2:
            lotto_num_generator()
        elif menu == 3:
            pig_latin()
        elif menu == 4:
            rock_paper_scissors()
    # Here, the function corresponding to the user's input is executed.
print(end='')
