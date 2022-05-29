"""
Modify this program, such that it gives the user only three chances to guess the
correct number. If they try three times without success, the program tells them
that they didn’t guess in time and then exits.
"""

import random

def guessing_game():
    answer = random.randint(0, 100)
    guess_num = 0

    while guess_num < 3:
        user_guess = int(input('What is your guess? '))
        guess_num += 1

        if user_guess == answer:
            print("Right! The answer is {}".format(user_guess))
            break

        if user_guess < answer:
            print('Your guess of {} is too low!'.format(user_guess))

        else:
            print('Your guess of {} is too high!'.format(user_guess))

guessing_game()
