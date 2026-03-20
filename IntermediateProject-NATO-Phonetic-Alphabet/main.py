import pandas
"""
NATO Phonetic Alphabet Converter (with Error Handling)

A script that converts a user entered word into its NATO phonetic alphabet
equivalent by looking up each letter in a dictionary built from the NATO
phonetic alphabet CSV dataset. This version extends the original converter
by wrapping the translation logic in a reusable function and adding error
handling for invalid non-alphabet characters.

Process:
    1. Reads the NATO phonetic alphabet dataset from 'nato_phonetic_alphabet.csv'
       into a pandas DataFrame containing two columns: 'letter' and 'code'.
    2. Converts the DataFrame into a dictionary using a dictionary
       comprehension with iterrows(), mapping each letter to its
       corresponding NATO phonetic code word.
       e.g. {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', ...}
    3. Calls generate_phonetic() to prompt the user for a word and
       translate it into NATO phonetic code words.

Functions:
    generate_phonetic(): Prompts the user to enter a word, converts it
                         to uppercase, and translates each letter into
                         its NATO phonetic code word using a list
                         comprehension. Handles invalid input by catching
                         KeyError exceptions for non-alphabet characters
                         and recursively calls itself to prompt the user
                         to try again.

Error Handling:
    Try:     Attempts to translate each character in the input word
             using the NATO dictionary.
    Except:  If a KeyError is raised (character not found in the
             dictionary, e.g. numbers, spaces, or special characters),
             prints an error message and recursively calls
             generate_phonetic() to prompt the user to enter a valid
             word containing only alphabet letters.
    Else:    If all characters are successfully translated, prints the
             list of NATO phonetic code words to the console.

Dependencies:
    pandas: Used to read the NATO phonetic alphabet CSV file and convert
            it into a dictionary via a DataFrame and iterrows().
"""

def generate_phonetic():
    #Create a list of the phonetic code words from a word that the user inputs.
    #Ensure characters are uppercase
    input_word = input("What word would you like translated?: ").upper()
    try:
        # Change to list comprehension to print the code for each letter in the word
        # new_list = [new_item for item in list]
        converted_code = [dict_nato[char] for char in input_word]
    except KeyError:
        print("Please only enter letters in the alphabet")
        # Call the function again
        generate_phonetic()
    else:
        print(converted_code )

#Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
#Read NATO csv and create a pandas dataframe
df_nato = pandas.read_csv('nato_phonetic_alphabet.csv')

#Create a new dictionary from the nato dataframe
# Change to dictionary comprehension with iterrows() method
# {new_key:new_value for (index, row) in df.iterrows()}
dict_nato  = {row.letter: row.code for (index, row) in df_nato.iterrows()}

generate_phonetic()