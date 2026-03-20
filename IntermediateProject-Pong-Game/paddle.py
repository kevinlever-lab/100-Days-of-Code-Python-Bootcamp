from turtle import Turtle

"""
Paddle Module

Defines the Paddle class used to create and manage the paddles in the
Pong game. Inherits from the Turtle class to render and move a paddle
on the game screen.
"""
# Constant to store the move distance for the paddle
MOVE_DISTANCE = 20

class Paddle(Turtle):
    """
       Represents a paddle in the Pong game.

       Inherits from Turtle to create a white vertical rectangular paddle
       that can move up and down on the screen. Used for both the left and
       right player paddles.
       """
    def __init__(self, position):
        """
        Initializes the Paddle object at the given screen position,
        oriented vertically as a tall white rectangle.
        """
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.position = position
        self.goto(position)

    def paddle_up(self):
        """
        Moves the paddle upward by MOVE_DISTANCE units (20) by setting
        the heading to north (90°) and moving forward.
        """
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def paddle_down(self):
        """
        Moves the paddle downward by MOVE_DISTANCE units (20) by setting
        the heading to south (270°) and moving forward.
        """
        self.setheading(270)
        self.forward(MOVE_DISTANCE)






