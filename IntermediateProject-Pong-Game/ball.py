from turtle import Turtle

"""
Ball Module

Defines the Ball class used to create and manage the ball in the Pong
game. Inherits from the Turtle class to render and move the ball across
the game screen, handling bouncing, speed, and position reset.
"""

class Ball(Turtle):
    """
    Represents the ball in the Pong game.

    Inherits from Turtle to create a white circular ball that moves
    across the screen, bouncing off walls and paddles. The ball
    progressively increases in speed with each paddle bounce and
    resets to the centre when a point is scored.
    """
    def __init__(self):
        """
        Initializes the Ball object as a white circle at the centre of
        the screen with a default movement of 10 units in both the x
        and y directions and a starting speed of 0.1 seconds.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.setposition(0,0)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Moves the ball one step in its current direction by adding
        x_move and y_move to the ball's current x and y coordinates.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        #When bouncing off top or bottom walls only y-cord is reversed
        #Multiply y_move by -1 to change direction
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the ball's horizontal direction by negating x_move
        and increases the ball's speed by reducing move_speed by 5%.
        Called when the ball collides with a paddle.
        """
        #When bouncing off left or right paddles only x-cord is reversed
        #Multiply x_move by -1 to change direction
        self.x_move *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        """
        Resets the ball to the centre of the screen (0, 0) and restores
        the default move speed of 0.1 seconds. Also reverses the
        horizontal direction via bounce_x() to serve towards the player
        who just scored a point.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()






