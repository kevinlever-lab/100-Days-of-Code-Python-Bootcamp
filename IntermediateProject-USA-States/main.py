import turtle
import pandas
"""
USA States Guessing Game

A graphical educational game built with Python's Turtle module where the
player attempts to name all 50 US states. Correct guesses are
displayed on an interactive map of the USA, and any missed states are saved
to a CSV file at the end of the game for further study.

Process:
    1. Reads the 50 states dataset from '50_states.csv', containing each
       state's name and its x/y coordinates on the map image.
    2. Sets up a graphical screen displaying a blank map of the USA.
    3. Repeatedly prompts the player to enter a state name until either:
          - All 50 states have been correctly guessed, or
          - The player types 'Exit' to end the game early.
    4. For each correct guess:
          - Adds the state to the list of guessed states.
          - Increments the score counter.
          - Retrieves the state's x/y coordinates from the dataset.
          - Displays the state name in red text at its correct location
            on the map.
    5. When the player exits or completes the game:
          - Compiles a list of all states not yet guessed.
          - Saves the missed states to 'states_to_learn.csv' for review.

Classes:
    StateManager: Manages the creation and display of correctly guessed
                  state labels on the map. Each state label is rendered
                  as a red text turtle at the state's map coordinates.

        Methods:
            new_state(): Creates a new turtle object and writes the
                         correctly guessed state name at its corresponding
                         x/y coordinates on the map.

Input:
    50_states.csv:          A CSV file containing each state's name and
                            its x/y coordinates on the blank map image,
                            with columns 'state', 'x', and 'y'.
    blank_states_img.gif:   A blank map of the USA used as the game
                            background image.

Output:
    states_to_learn.csv:    A CSV file containing a list of all states
                            the player failed to guess, saved when the
                            player exits the game, with the column
                            heading 'Missed States'.

Dependencies:
    turtle:  Used to set up the graphical screen, display the blank map
             image, and render correctly guessed state names on the map.
    pandas:  Used to read the states dataset, look up state coordinates,
             and export the missed states list to a CSV file.
"""
state_data = pandas.read_csv('50_states.csv')
#Create a list of all the states from the dataframe
all_states = state_data.state.to_list()
screen = turtle.Screen()
screen.title("USA States Game")
image="blank_states_img.gif"
screen.addshape(image)

class StateManager():
    def __init__(self):
        self.message = ""

    #def new_state(self, xpos, ypos, state):
    def new_state(self):
        new_state = turtle.Turtle(shape="square")
        new_state.shapesize(stretch_wid=5, stretch_len=1)
        new_state.penup()
        new_state.color("red")
        new_state.hideturtle()
        new_state.xcord = x_cord
        new_state.ycord = y_cord
        new_state.message = check_answer
        new_state.goto(new_state.xcord, new_state.ycord)
        new_state.pendown()
        new_state.write(arg=new_state.message, move=False, align="center", font=('Arial', 10, 'normal'))

#Create turtle object to display state name
state_manager = StateManager()

#Create the map
turtle.shape(image)
score = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What is another state's name?")

    # Ensure answer id title case
    check_answer = answer_state.title()

    #End the game if user enters 'exit'
    if check_answer == "Exit":
        #missed_states = []
        #Initial code before list comprehension
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        #Code using list comprehension
        missed_states = [state for state in all_states if state not in guessed_states]

        #Create a dataframe so the list can be exported. Add column heading 'Missed States'
        df_missed_states = pandas.DataFrame(missed_states, columns=['Missed States'])
        #Write df to csv
        df_missed_states.to_csv("states_to_learn.csv")
        break

    if check_answer in state_data["state"].values:
        #Add the state to the list of guessed states
        guessed_states.append(check_answer)
        #Increment score
        score += 1
        #.item() is required to get the value only and not the additional metadata
        x_cord = state_data[state_data["state"] == check_answer]["x"].item()
        y_cord = state_data[state_data["state"] == check_answer]["y"].item()

        #Display the state on the map
        state_manager.new_state()




