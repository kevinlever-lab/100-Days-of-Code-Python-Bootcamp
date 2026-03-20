from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

"""
Password Manager (with JSON Storage and Search)

A graphical password manager application built with Python's Tkinter
module that generates secure random passwords, saves website credentials
to a JSON file, searches for previously saved credentials by website
name, and automatically copies generated passwords to the clipboard.

Process:
    1. When the Generate Password button is clicked:
          - Randomly generates a secure password containing:
              8-10 random uppercase and lowercase letters.
              2-4 random symbols from a predefined set.
              2-4 random numbers.
          - Shuffles all characters to produce a randomised password.
          - Inserts the generated password into the password field.
          - Automatically copies the password to the clipboard.
    3. When the Add button is clicked:
          - Validates that all fields (website, email/username, password)
            have been filled in, displaying a warning if any field is
            empty.
          - Attempts to read existing credentials from 'data.json':
              If the file exists, updates it with the new entry.
              If the file does not exist, creates a new JSON file with
              the new entry.
          - Saves credentials to a JSON file
          - Clears the website and password fields after saving.
    4. When the Search button is clicked:
          - Validates that the website field has been filled in,
            displaying a warning if it is empty.
          - Attempts to read credentials from 'data.json':
              If the file does not exist, displays an error dialog.
              If the website is found, populates the email/username
              and password fields with the stored credentials.
              If the website is not found, displays an error dialog.

Functions:
    genpwd_clicked():  Generates a random secure password, inserts it
                       into the password field, and copies it to the
                       clipboard.
    savepwd_clicked(): Validates all input fields and saves the entered
                       credentials to the JSON data file, creating the
                       file if it does not already exist.
    find_password():   Searches the JSON data file for credentials
                       matching the entered website name and populates
                       the email/username and password fields with the
                       retrieved data.

Dependencies:
    tkinter:    Used to build the graphical user interface, including
                the window, canvas, labels, entry fields, and buttons.
    messagebox: Used to display warning and error dialogs.
    random:     Used to randomly generate password characters.
    pyperclip:  Used to copy the generated password to the clipboard.
    json:       Used to read, update, and write credentials to the
                JSON data file.
"""
FONT_NAME = "Courier"
# Change file type to json
DATA_FILE = "data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genpwd_clicked():
    """
    Builds a password by randomly selecting characters from three
    separate character sets (letters, symbols, and numbers), combining
    them into a single list, shuffling the result to ensure randomness,
    and joining the characters into a final password string.

    Password Composition:
        Letters: 8-10 randomly selected uppercase and lowercase letters
                 from a-z and A-Z.
        Symbols: 2-4 randomly selected symbols from the set:
                 ! # $ % & ( ) * +
        Numbers: 2-4 randomly selected digits from 0-9.
        Total:   12-18 characters, shuffled to randomise character order.

    Updates:
        pwd_entry (Entry): Clears any existing content and inserts the
                           newly generated password at position 0 of
                           the password entry field.
        clipboard:         Copies the generated password to the system
                           clipboard via pyperclip for immediate use
                           without needing to manually select and copy.
    """
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    #update form
    pwd_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savepwd_clicked():
    """
    Retrieves the current values from the website, email/username, and
    password entry fields and structures them as a nested dictionary.
    Validates that all fields have been filled in before attempting to
    save. Handles both the creation of a new data file and updating of
    an existing file, ensuring previously saved credentials are
    preserved.

    Data Structure:
        Credentials are saved to the JSON file in the following format:
            {
                "website": {
                    "email": "email/username",
                    "password": "password"
                }
            }

    Validation:
        If any of the three fields (website, email/username, password)
        are empty, a warning dialog is displayed prompting the user to
        fill in all fields. No data is saved until all fields contain
        a value.

    File Handling:
        Try:     Attempts to open and read the existing JSON data file.
        Except:  If the file does not exist (FileNotFoundError), creates
                 a new JSON data file and writes the new entry.
        Else:    If the file exists, updates the existing data with the
                 new entry and overwrites the file with the merged data,
                 preserving all previously saved credentials.
        Finally: Clears the website and password entry fields regardless
                 of whether the save succeeded or a new file was created,
                 leaving the email/username field unchanged for
                 convenience when adding multiple entries for the same
                 user.

    Displays:
        Warning dialog: If any input field is empty, prompting the
                        user to fill in all required fields.

    Dependencies:
        json:       Used to read, update, and write credentials to
                    the JSON data file.
        messagebox: Used to display the warning dialog when validation
                    fails.
    """
    website = website_entry.get()
    uname = uname_entry.get()
    password = pwd_entry.get()
    new_data = {
        website: {
            "email": uname,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0 or len(uname) == 0:
        messagebox.showwarning(title="Warning", message="Please enter all fields")
    else:
        try:
            with open(DATA_FILE, "r") as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(DATA_FILE, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            # Write the data to file
            with open(DATA_FILE, "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Delete form entries
            website_entry.delete(0, END)
            pwd_entry.delete(0, END)

# ---------------------------- search function ------------------------ #
def find_password():
    """
    Searches the JSON data file for stored credentials matching the
    entered website name and populates the email/username and password
    fields with the retrieved data when the Search button is clicked.

    Validation:
        If the website field is empty, a warning dialog is displayed
        prompting the user to enter a website URL.

    File Handling:
        Try:     Attempts to open and read the JSON data file.
        Except:  If the file does not exist (FileNotFoundError),
                 displays an error dialog notifying the user that
                 no data file was found.
        Else:    If the file exists, checks whether the entered website
                 has a matching entry in the data:
                     Found:     Retrieves the stored email and password
                                for the website.
                     Not Found: Displays an error dialog notifying the
                                user that no details exist for the
                                entered website.
        Finally: Clears the email/username and password entry fields,
                 then populates them with the retrieved credentials.
                 If no credentials were found, both fields are left
                 empty.

    Displays:
        Warning dialog: If the website field is empty, prompting the
                        user to enter a website URL.
        Error dialog:   If the data file does not exist, or if no
                        credentials are found for the entered website.

    Dependencies:
        json:       Used to read and parse the JSON data file.
        messagebox: Used to display warning and error dialogs.
    """
    website = website_entry.get()
    email = ""
    password = ""
    if len(website) == 0:
        messagebox.showwarning(title="Warning", message="Please enter the web site URL")
    else:
        try:
            with open(DATA_FILE, "r") as data_file:
                # Read old data
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No Data File Found")
        else:
            # Check if website data is stored in the file
            if website in data:
                password = data[website]['password']
                email = data[website]['email']
            else:
                messagebox.showwarning(title="Error", message="No details for the website exist")
        finally:
            # First clear the email and password form entries
            uname_entry.delete(0, END)
            pwd_entry.delete(0, END)
            # update form with values retrieved
            pwd_entry.insert(0, password)
            uname_entry.insert(0,email)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady =50, bg="white")  #Extra padding of the window around the canvas which is 200x200

canvas = Canvas(width=200, height = 200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
#Set the image in the middle of the canvas (x, y) -> (100, 100)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 13, "normal"), bg="white")
website_label .grid(column=0, row=1)

uname_label = Label(text="Email/Username:", font=(FONT_NAME, 13, "normal"), bg="white")
uname_label .grid(column=0, row=2)
pwd_label = Label(text="Password:", font=(FONT_NAME, 13, "normal"), bg="white")
pwd_label .grid(column=0, row=3)

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
#Place cursor
website_entry.focus()
uname_entry = Entry(width=50)
uname_entry.grid(column=1, row=2, columnspan=2)
#Insert initial value
uname_entry.insert(0,"kevin@gmail.com")
pwd_entry = Entry(width=32)
pwd_entry.grid(column=1, row=3)

genpwd_button = Button(text="Generate Password", highlightthickness=0, command=genpwd_clicked, bg="white")
genpwd_button.grid(column=2, row=3)
add_button = Button(text="Add", highlightthickness=0, command=savepwd_clicked,width=43, bg="white")
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", highlightthickness=0, command=find_password, bg="white", width=14)
search_button .grid(column=2, row=1)

#Keep the window displayed
window.mainloop()




