from turtle import Turtle, Screen
import random

"""
Turtle Racing Game

A graphical turtle racing game built with Python's Turtle module where
the player bets on which coloured turtle will win the race.

Process:
    1. Sets up a 500x400 graphical screen using the Turtle Screen module.
    2. Prompts the player to place a bet by selecting a turtle colour
       (red, orange, yellow, green, blue, or purple).
    3. Each turtle advances a random distance (0-10 units) per turn,
       simulating an unpredictable race.
    4. The race ends when the first turtle crosses the finish line at
       the right side of the screen (x > 230).
    5. Announces the winning turtle's colour and whether the player
       won or lost their bet.

"""
race_on=False
screen = Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? \nEnter a colour (red, orange, yellow, green, blue, purple): ")

# List of turtle colours
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
# List to store turtle objects
all_turtles = []
#create and position a turtle for each colour
#Vertical separation between each turtle
vertsep=0
for col in colours:
    # Since creating an object for each turtle, no need to assign a name
    # Store each turtle object in a list - all_turtles[]
    # Create a turtle object for each colour
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(col)
    new_turtle.penup()
    # Set starting position
    new_turtle.goto(-230, -125 + vertsep)
    vertsep+=50
    all_turtles.append(new_turtle)

if user_choice:
    race_on = True

while race_on:
    for turtle in all_turtles:
        #Turtle width (40), screen width (250), so stop race when turtle reaches 250 - 40/2 so we can see the turtle
        if turtle.xcor() > 230:
            race_on=False
            winning_colour=turtle.pencolor()
            if winning_colour==user_choice:
                print(f"You won the bet!. The {winning_colour} turtle is the winner!")
            else:
                print(f"You lost the bet!. The {winning_colour} turtle is the winner!")

        #Move each turtle a random distance
        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)

screen.exitonclick()

