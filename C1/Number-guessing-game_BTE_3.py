import random

def guessing_game():
    mylist = ["apple", "banana", "cherry"]
    answer = random.choice(mylist)
    guess_num = 0

    while guess_num < 3:
        user_guess = str(input('Pick a fruit. What is your guess? '))
        guess_num += 1 

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess {user_guess} is not correct!')

        else:
            print(f'Your guess {user_guess} is not correct!')

guessing_game()

    
            

        
