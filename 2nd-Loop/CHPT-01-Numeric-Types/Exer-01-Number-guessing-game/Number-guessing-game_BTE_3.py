"""
Try the same thing, but have the program choose a random word from the dic-
tionary, and then ask the user to guess the word. (You might want to limit your-
self to words containing two to five letters, to avoid making it too horribly
difficult.) Instead of telling the user that they should guess a smaller or larger
number, have them choose an earlier or later word in the dict.
"""
import random

def guessing_game():
    mylist = ["apple", "banana", "cherry"]
    answer = random.choice(mylist)
    guess_num = 0

    while guess_num < 3:
        user_guess = str(input("Pick a fruit. What is your guess? "))
        guess_num += 1

        if user_guess == answer:
            print("Right! The answer is {}".format(user_guess))
            break

        if user_guess < answer:
            print("Your guess {} is not correct!".format(user_guess))
        
        else:
            print("Your guess {} is not correct!".format(user_guess))
    
guessing_game()