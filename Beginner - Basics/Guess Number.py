import guess_number_art
import random

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

