'''
Mastermind game! There are 6 option colors and you have to guess the random sequence of 4 colors.
Each try you'll get tips of the correct and incorrect positions.
But remember: there are only 10 tries!
Good Luck!
'''

import random

COLORS = ['R', 'G', 'B', 'Y', 'P', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for i in range(CODE_LENGTH):
        item = random.choice(COLORS)
        code.append(item)

    return code

def guess_code(): 
    while True:
        guess = input('Guess the code: ').upper().split(' ')
        if len(guess) != CODE_LENGTH:
            print(f'You must enter {CODE_LENGTH} colors!')
            continue

        for color in guess:
            if color not in COLORS:
                print(f'Invalid color: {color}. Try again!')
                break
        else:  
            break
        # If I didn't break, this 'else' breaks the while loop
        # That means ALL the colors are valid (are in COLORS)

    return guess

def check_code(guess, real_code):
    color_counts = {}  
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code: 
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color: 
            correct_pos += 1
            color_counts[guess_color] -= 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f'Welcome to Mastermind! You have {TRIES} tries to guess the code')
    print('The valid colors are:', *COLORS)

    code = generate_code() 
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        if correct_pos == CODE_LENGTH:
            print(f'You guessed the code in {attempts} tries!')
            break

        print(f'Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}')
    else:
        print('You ran out of tries. The code was:', *code)
        # *code - prints every element of the list space-separeted 

    while True:
        answer = int(input('Do you wanna play again? 1 - YES | 2 - NO: '))
        if answer == 1 or answer == 2:
            break
        print('Invalid answer!')
    if answer == 1: 
        game()
    else: 
        print('See you soon...')

if __name__ == '__main__': 
    game()
    