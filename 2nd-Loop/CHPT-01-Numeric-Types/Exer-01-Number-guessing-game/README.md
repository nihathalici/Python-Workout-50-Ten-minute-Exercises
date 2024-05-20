```python
import random

def guessing_game():

    answer = random.randint(0, 100)

    while True:
        user_guess = int(input("What is your guess? "))

        if user_guess == answer:
            print("Right! The answer is {}".format(user_guess))
            break

        if user_guess < answer:
            print("Your guess of {} is too low!".format(user_guess))

        else:
            print("Your guess of {} is too high!".format(user_guess))

guessing_game()
```
