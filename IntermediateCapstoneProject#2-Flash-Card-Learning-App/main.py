from tkinter import *
from tkinter import messagebox
import pandas
import random
import os

"""
Language Flash Card Application

A graphical French-to-English flash card learning application built with
Python's Tkinter module that presents random French words, automatically
flips to reveal the English translation after 3 seconds, and tracks
unknown words by saving them to a CSV file for future study sessions.

Process:
    1. Attempts to load previously unlearned words from 'words_to_learn.csv'.
       If the file does not exist, loads the full French word list from
       'french_words.csv' instead.
    2. Converts the loaded DataFrame into a list of dictionaries in the
       format: {'French': 'French word', 'English': 'English word'}.
    3. Sets up a graphical window displaying a flash card canvas and two
       buttons (correct and unsure) below the card.
    4. Starts the lesson by displaying a random French word on the front
       card and automatically flipping to the English translation after
       3 seconds.
    5. The player responds using one of two buttons:
          - Correct (✔): The word pair is removed from the learning list,
                         the updated list is saved to 'words_to_learn.csv',
                         and a new random word is displayed.
          - Unsure  (✘): The current card timer is cancelled and a new
                         random word is displayed without removing the
                         current word from the learning list.
    6. When all words have been correctly identified:
          - Deletes 'words_to_learn.csv' if it exists.
          - Displays a completion dialog prompting the user to restart
            the application.

Functions:
    new_word():        Cancels the active card timer, selects a random
                       word pair from the learning list, displays the
                       French word on the front card, and starts a new
                       3-second timer to flip to the English translation.
    change_card():     Flips the card to display the English translation
                       on the back card with white text.
    correct_clicked(): Removes the current word pair from the learning
                       list, saves the updated list to 'words_to_learn.csv',
                       and loads a new word. Displays a completion message
                       and deletes the CSV file when all words are learned.

File Handling:
    Input:
        data/french_words.csv:    The full French-English word list used
                                  on the first run of the application.
        data/words_to_learn.csv:  The filtered list of words not yet
                                  correctly identified, loaded on
                                  subsequent runs if it exists.
    Output:
        data/words_to_learn.csv:  Updated and saved each time a word is
                                  correctly identified, containing only
                                  the remaining unlearned word pairs.
                                  Deleted when all words are learned.

Dependencies:
    tkinter:    Used to build the graphical user interface, including
                the window, canvas, buttons, and card text.
    messagebox: Used to display the lesson completion dialog.
    pandas:     Used to read the word list CSV files, convert the data
                to a list of dictionaries, and save the updated learning
                list back to CSV.
    random:     Used to randomly select a word pair from the learning
                list for each new flash card.
    os:         Used to check for and delete the 'words_to_learn.csv'
                file when all words have been correctly identified.
"""

BACKGROUND_COLOR = "#B1DDC6"
# Initialize dictionary
random_pair ={}
# Initialize dataframe
df_data = pandas.DataFrame()

# Read csv file into a dataframe using pandas
# The first time the program is run, import the french_words.csv
# If the words_to_learn.csv file is available, import this list of words
try:
    df_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df_data = pandas.read_csv("data/french_words.csv")
finally:
    # Convert the dataframe to a dictionary
    # Format {'French': 'French word', 'English: 'English word'}
    data_dict = df_data.to_dict(orient="records")
    #print(data_dict)

#----- Functions -----#
def new_word():
    global random_pair, card_timer
    # Cancel the current 3-second timer for cases where the user clicked a button
    window.after_cancel(card_timer)
    #Get a random (key, value) tuple
    random_pair = random.choice(data_dict)
    #print(f"French card - French: {random_pair["French"]}, English: {random_pair["English"]}")
    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_pair["French"], fill="black")
    # Switch cards from French to English after 3 seconds
    card_timer = window.after(3000, func=change_card)

def change_card():
    #Change the language to English and change to English card
    global random_pair
    language = "English"
    # print(f"English card - French: {random_pair["French"]}, English: {random_pair["English"]}")
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_pair["English"], fill="white")
    language = "French"

def correct_clicked():
    global random_pair
    # Word is correctly translated, so remove word pair from the dictionary
    data_dict.remove(random_pair)
    # Save the list of unknown words to a file if the dictionary is not empty
    # Save dictionary as a dataframe then save the dataframe to csv file
    if data_dict: # checks that the dictionary is not empty
        df_words_to_learn = pandas.DataFrame(data_dict)
        # Dont include index - index=false
        df_words_to_learn.to_csv("data/words_to_learn.csv", index=False)
        # Get a new word
        new_word()
    else: # remove words_to_learn.csv file if it exists as user knows all the words
        if os.path.exists("data/words_to_learn.csv"):
            os.remove("data/words_to_learn.csv")
        # User knows all the words and none left to learn
        # Pop up indicating no more words to learn and to start again
        messagebox.showwarning(title="Lesson Over", message="All words have been correctly selected. Please restart the application.")

#----- UI Setup -----#
window = Tk()
window.title("Language Flash Card")
window.config(padx=50, pady=50, width = 800, height= 526,bg = BACKGROUND_COLOR)

# Switch cards from French to English after 3 seconds. Assign a timer so it can be cancelled when button is clicked
card_timer = window.after(3000, func=change_card)
# Flash card images
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
cross_image = PhotoImage(file="images/wrong.png")
tick_image = PhotoImage(file="images/right.png")
# Flash card buttons
unsure_button = Button(image = cross_image , highlightthickness = 0, command = new_word)
correct_button = Button(image = tick_image , highlightthickness = 0, command = correct_clicked)

#Set the image in the middle of the canvas
canvas=Canvas(width = 800, height= 526)
card_background = canvas.create_image(400, 263, image = front_image)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(column=0, row = 0, columnspan = 2)
#Set buttons below the card image
unsure_button.grid(column=0, row = 1)
correct_button.grid(column=1, row = 1)
#Card text
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Start the lesson
new_word()

#Keep the window displayed
window.mainloop()
