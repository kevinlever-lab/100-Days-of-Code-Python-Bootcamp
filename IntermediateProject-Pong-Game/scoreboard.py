from turtle import Turtle

"""
Scoreboard Module

Defines the Scoreboard class used to display and manage the scores for
both players in a Pong game. Inherits from the Turtle class to render
scores directly on the game screen.
"""

class Scoreboard(Turtle):
    def __init__(self):
        """
        Initializes the Scoreboard with both player scores set to zero,
        hides the turtle cursor, and displays the initial scoreboard.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh_scoreboard()

    #Refresh scoreboard with new score after clearing current score first
    def refresh_scoreboard(self):
        """
        Clears the current scoreboard display and rewrites both player
        scores at the top of the screen.
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))


    def l_point(self):
        """
        Increments the left player's score by one and refreshes
        the scoreboard display to reflect the updated score.
        """
        self.l_score += 1
        self.refresh_scoreboard()

    def r_point(self):
        """
        Increments the right player's score by one and refreshes
        the scoreboard display to reflect the updated score.
        """
        self.r_score += 1
        self.refresh_scoreboard()


