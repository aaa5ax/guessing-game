from analyticskit import *
import random

while True:
    secret_number = random.randint(1, 10)
    number = single_input('Guess a number between 1 and 10.')

    if number == secret_number:
        show_message('You win!', f'You guessed the correct number')
    else:
        show_message('You lose', f'The correct number was {secret_number}')

    play = single_input('Would you like to play again? Enter y/n.')
    if play == 'n':
        break