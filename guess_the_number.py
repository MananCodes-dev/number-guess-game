import random

number = random.randint(1, 10)
attempts = 3

print("Welcome to 'Guess the Number'! choose between 1 to 10 any number")

while attempts > 0:
    guess = int(input('Enter your guess :'))
    if guess == number:
        print("Congratulations! You've guessed the number correctly.")
        break
    elif guess < number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
    attempts -= 1

if attempts == 0:
    print(f"Sorry, you've run out of attempts. The number was {number}.")