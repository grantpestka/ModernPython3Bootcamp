import random

play = True
while play == True:
    this_round = True
    random_number = random.randint(1,10)
    prompt = 'Guess a number between 1 and 10: '
    while this_round == True:
        user_guess = int(input(f'{prompt}'))
        if user_guess == random_number:
            this_round = False
            print('You guessed right!!!')
        else:
            if user_guess > random_number:
                err_dir = 'high'
            else:
                err_dir = 'low'
            this_round = True
            prompt = f'Too {err_dir} Guess again: '
    play_again = ''
    while play_again == '':
        play_again = input(f'Play again?(y/n): ').lower()
        if play_again == 'n':
            play = False
        elif play_again == 'y':
            play = True
        else:
            print('please enter "y" or "n"')
            play_again = ''
        
print('Thanks for playing!')
