# Project 4: Number Guessing Game
# Generates a random number and asks the user to guess it
# Built with Python using random module and while loop

import random

print("--- Number Guessing Game ---")
secret_number = random.randint(1, 9)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 9: "))
    attempts += 1

    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempt(s).")
        break


# Project 5: Multiplication Table Generator
# Generates a multiplication table for any number entered by the user
# Built with Python using a for loop and f-strings

print("\n--- Multiplication Table Generator ---")
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
