"""

This program is a number guessing game

"""

from typing import Tuple
import random
import os

def clear():
    return os.system('cls')

def pause():
    return os.system('pause')

# Easily creates the needed parameters for the guessing game, should be unpacked on guess_number()
def create_difficulty(min_range: int, max_range: int, change: bool) -> tuple:
    range_num = (min_range, max_range)
    range_string = f'{min_range}-{max_range}'
    return (random.randint(min_range, max_range), change, range_num, range_string)

# Simple number guessing game loop. If 'change' is True, will change the guessable number every try. If 'debug' is True, will show the number.
def guess_number(number: int, change: bool, range_num: Tuple[int, int], range_string: str, debug=False):
    clear()

    while True:
        if change:
            number = random.randint(*range_num)

        try:
            if debug:
                print(number)

            number_guessed = int(input(f'CAN YOU GUESS THE NUMBER? ({range_string})\n\n'))
        except(ValueError):
            number_guessed = None

        if number_guessed == number:
            print('\nYOU WIN\n')
            pause()
            clear()
            break
        else:
            print('\nNOOOOOOOOOOOOOOO\n')
            os.system('pause')
            clear()

# Keys are tuples so they can be multipurpose. Values should be unpacked on create_difficulty().
# New difficulties can be added as long as they follow the standard
difficulty_select = {('[E]asy', 'E', 'EASY'): (1, 10, False),
                     ('[N]ormal', 'N', 'NORMAL'): (1, 100, False),
                     ('[H]ard', 'H', 'HARD'): (1, 10, True), 
                     ('[I]nsane', 'I', 'INSANE'): (1, 100, True)}
difficulty_text = ''

for difficulty_name in difficulty_select.keys():
    difficulty_text += f'{difficulty_name[0]} '

while True:
    clear()
    difficulty_selected = input(f'GUESS THE NUMBER\n----------------\nSELECT THE DIFFICULTY OR TYPE "EXIT":\n\n{difficulty_text}\n\n').upper()

    if difficulty_selected == 'EXIT':
        clear()
        print('THANKS FOR PLAYING!')
        break

    for difficulty_name in difficulty_select.keys():
        if difficulty_selected in difficulty_name:
            guess_number(*create_difficulty(*difficulty_select[difficulty_name]))