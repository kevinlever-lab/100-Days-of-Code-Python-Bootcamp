"""
Mail Merge Letter Generator

A mail merge script that generates personalised invitation letters for
each recipient by replacing a placeholder name in a template letter with
each invited guest's actual name and saving the completed letters as
individual text files ready to send.

Process:
    1. Reads the list of invited guest names from 'invited_names.txt',
       storing each name as an item in a list.
    2. Reads the template letter from 'starting_letter.txt', storing
       each line as an item in a list.
    3. Strips extra whitespace and newline characters from each line of
       the template letter to remove additional blank lines introduced
       by readlines().
    4. Replaces the sign-off name 'Angela' with 'Kevin' in the last
       line of the template letter.
    5. For each invited guest:
          a. Strips whitespace and newline characters from the name.
          b. Creates a copy of the template letter.
          c. Replaces the '[name]' placeholder in the first line with
             the guest's actual name.
          d. Saves the personalised letter as a new text file named
             'letter_for_<name>.txt' in the 'Output/ReadyToSend' folder.

File Structure:
    Input:
        Input/Letters/starting_letter.txt  - Template letter with a
                                             '[name]' placeholder in
                                             the first line.
        Input/Names/invited_names.txt      - List of invited guest names,
                                             one name per line.
    Output:
        Output/ReadyToSend/letter_for_<name>.txt - Personalised letter
                                                   for each invited guest.
"""
#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Constants for directors and files
STARTING_LETTER = "Input/Letters/starting_letter.txt"
INVITED_NAMES = "Input/Names/invited_names.txt"
READY_SEND = "Output/ReadyToSend"
NEW_FILENAME = "letter_for_"

#Get list of names from invited_names.txt and store the names in a list invited_names[]
#The readlines() method returns a list containing each line in the file as a list item
#Close the file once read
names_file = open(INVITED_NAMES, "r")
invited_names =  names_file.readlines()
names_file.close()

#Open the starting letter and read each line into a list
#Close the file once read
start_letter_file = open(STARTING_LETTER, "r")
start_letter_contents =  start_letter_file.readlines()
start_letter_file.close()
num_lines = len(start_letter_contents)
print (start_letter_contents)

#After readlines() there are 3 blank lines instead of 1 blank line between each line in the letter
#Strip each line to remove the additional blank lines
for x in range(0, num_lines):
    stripped_line = start_letter_contents[x].strip()
    start_letter_contents[x] = stripped_line

#Replace Angela with Kevin in the last line of the letter
goodbye = start_letter_contents[num_lines-1].replace("Angela", "Kevin")
start_letter_contents[num_lines-1] = goodbye


#Retrieve each name the list invited_names
num_names = len(invited_names)
for i in range(0, num_names):
    #Strip spaces and '/n' from the name
    stripped_name = invited_names[i].strip()
    #Concatenate the filename
    new_letter_file = NEW_FILENAME + stripped_name + ".txt"
    #create a new letter by copying starting letter, resetting first line
    #Copy starting letter
    new_invitation = start_letter_contents[:]
    # Replace the [name] in the first line of the starting letter
    new_intro = new_invitation[0].replace("[name]", stripped_name)
    new_invitation[0] = new_intro

    #Create a new letter
    letter_name = READY_SEND + "/" + new_letter_file
    with open(letter_name, mode="a") as file:
        #Write each line of the invitation
        for j in range(0, num_lines):
            #Add new line character
            line_entry = new_invitation[j] + "\n"
            file.write(line_entry)


