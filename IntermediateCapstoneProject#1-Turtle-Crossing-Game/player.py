from turtle import Turtle

"""
Player Module

Defines the Player class used to create and manage the player's turtle
in the Turtle Crossing game. Inherits from the Turtle class to render
and control the player's movement up the screen toward the finish line.
"""

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """
    Represents the player's turtle in the Turtle Crossing game.

    Inherits from Turtle to create a black turtle shape that starts at
    the bottom of the screen and moves upward toward the finish line
    at the top of the screen. Detects when the finish line has been
    reached and supports resetting to the starting position at the
    start of each new level.
    """

    def __init__(self):
        """
        Initializes the Player turtle at the bottom centre of the screen,
        ready to move toward the finish line.
        """
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y

    def move_up(self):
        """
        Moves the player turtle forward (upward) by MOVE_DISTANCE (10)
        units each time the Up arrow key is pressed.
        """
        self.forward(MOVE_DISTANCE)


    def goto_start(self):
        """
        Returns the player turtle to the starting position at the bottom
        centre of the screen at the beginning of each new level.
        """
        self.goto(STARTING_POSITION)


    def reached_finish_line(self):
        """
        Checks whether the player turtle has reached or passed the finish
        line at the top of the screen.
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

