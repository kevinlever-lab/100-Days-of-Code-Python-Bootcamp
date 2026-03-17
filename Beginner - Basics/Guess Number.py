import guess_number_art
import random

"""
Number Guessing Game

A command-line game where the player tries to guess a randomly generated number
between 1 and 100 within a limited number of attempts.

Process:
    1. Prompts the player to choose a difficulty level:
        - 'easy': grants 10 guesses.
        - 'hard': grants 5 guesses.
    3. Randomly generates a number between 1 and 100.
    4. Repeatedly prompts the player to guess the number until:
        - The player guesses correctly and wins, or
        - The player runs out of guesses and loses.
    5. After each incorrect guess, hints are provided:
        - 'Too low'  - if the guess is below the target number.
        - 'Too high' - if the guess is above the target number.

Functions:
    initialize_game(): Displays the logo, sets and returns the number of guesses
                       based on the chosen difficulty level.
    user_guess(guesses): Displays remaining guesses, prompts the player for a
                         guess and returns the entered number.
"""

game_over = False


# Initialize the game by asking for the difficulty level
def initialize_game():
    print(guess_number_art.logo)
    difficulty_level = 0
    # User chooses difficulty level
    print("Welcome to the number guessing game. Guess a number between 1 and 100.")
    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
    if difficulty.lower() == "easy":
        difficulty_level = 10
        return difficulty_level
    elif difficulty.lower() == "hard":
        difficulty_level = 5
        return  difficulty_level
    else:
        print("You have entered an incorrect response!")
        return difficulty_level

# Get user guess
def user_guess(guesses):
    # Compare numbers
    print(f"You have {guesses} remaining to guess the number.")
    # User chooses a number
    user_num = int(input("Make a guess: "))
    return user_num

# Start of the program
# Computer chooses a number 1-100
computer_num = random.randint(1, 100)

# Initialize game by asking for the difficulty level
user_guesses = int(initialize_game())
if user_guesses == 0:
    game_over = True

# User repeatedly chooses numbers
while not game_over:
    user_guessed = user_guess(user_guesses)
    user_guesses -= 1
    # Compare guessed value
    if user_guessed ==  computer_num:
        print(f"You got it! The answer was {computer_num}.")
        game_over = True
    elif user_guessed <  computer_num:
        print("Too low.")
        if user_guesses == 0:
            print("You have run out of guesses, you lose.")
            game_over = True
        else:
            print("Guess Again.")
    else: # user_guessed >  computer_num
        print("Too high.")
        if user_guesses == 0:
            print("You have run out of guesses, you lose.")
            game_over = True
        else:
            print("Guess Again.")

