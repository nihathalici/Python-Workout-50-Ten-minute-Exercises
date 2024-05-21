```python
import random

def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')

guessing_game()
```

* 'Modify this program, such that it gives the user only three chances to guess the correct number.
If they try three times without success, the program tells them that they didn’t guess in time and then exits.


```python
import random

def guessing_game():
    answer = random.randint(0, 100)
    guess_num = 0

    while guess_num < 3:
        user_guess = int(input('What is your guess? '))
        guess_num += 1 

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')

guessing_game()
```
