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

* Not only should you choose a random number, but you should also choose a random number base, from 2 to 16, in which the user should submit their input. If the user inputs “10” as their guess, you’ll need to interpret it in the correct number base; “10” might mean 10 (decimal), or 2 (binary), or 16 (hexadecimal).
```python
def guessing_game():
  answer = random.randint(0, 100)
  required_base = random.choice([2, 8, 10, 16])  # binary/octal/decimal/hex

  while True:
    user_guess = int(input('What is your guess? '), required_base)

    if user_guess == answer:
      print(f'Right! The answer is {user_guess}')
      break
    
    if user_guess < answer:
      print(f'Your guess of {user_guess} is too low!')
    
    else:
      print(f'Your guess of {user_guess} is too high!')

guessing_game()
```
