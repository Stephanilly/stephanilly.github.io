#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from guess_art import logo
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


# Set the number to guess
def answer_number():
    number = random.randint(1, 100)
    return number


# Compare the user's guess with the answer
def compare(guess, number, attempts):
    if guess > number:
        print("Too high.")
        return attempts - 1
    elif guess < number:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {number}.")
        return


# Define the number of guesses based on difficulty level
def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5


# Define the game
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = answer_number()
    attempts = difficulty()
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = compare(guess, number, attempts)
    while guess != number and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = compare(guess, number, attempts)
    if attempts == 0:
        print(f"You've run out of guesses, you lose. The number was {number}.")
        return


game()

# Give the player a choice to play again
while input("Do you want to play again? y or n: ") == "y":
    clear()
    game()
