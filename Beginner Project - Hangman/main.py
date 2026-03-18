import random

"""
Hangman Game

A command-line Hangman word guessing game where the player tries to guess a
hidden word one letter at a time before running out of lives.

Process:
    1. Randomly selects a word from the word list in `hangman_words` module.
    3. Displays the word as a series of underscores representing each letter.
    4. Gives the player 6 lives at the start of the game.
    5. Repeatedly prompts the player to guess a letter until:
        - The player correctly guesses all letters in the word and wins, or
        - The player runs out of lives and loses.
    6. After each guess:
        - Notifies the player if the letter was already guessed previously.
        - Reveals correctly guessed letters in their position within the word.
        - Deducts a life for each incorrect guess and notifies the player.
        - Displays the current Hangman stage illustration based on lives remaining.
    7. Announces the result at the end of the game:
        - Win: Congratulates the player.
        - Lose: Reveals the correct word to the player.

Dependencies:
    hangman_words: Provides the word list used to randomly select the hidden word.
    hangman_art:   Provides the logo displayed at the start of the game and the
                   Hangman stage illustrations displayed after each incorrect guess.
"""


# Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    # Tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letters:
        print("You have already guessed that letter!")
    else:
        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)


        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed the letter '{guess}' which is not in the word. You lose a life")

            if lives == 0:
                game_over = True

                # Let the user know the correct word they were trying to guess.
                print(f"***********************YOU LOSE**********************")
                print(f"The correct word is: '{chosen_word}'")
        # If all letters are guessed
        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        # Display the stage from the file hangman_art.py
        print(hangman_art.stages[lives])

    guessed_letters.append(guess)
