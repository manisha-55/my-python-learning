#Project 1: Number Guessing Game
import random
secret_num = random.randint(1, 100)
while True:
    guess = int(input("Enter your guess (between 1 and 100): "))
    if guess < secret_num:
        print("Too low! Try again.")
    elif guess > secret_num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break