from turtle import Turtle

"""
Scoreboard Module

Defines the Scoreboard class used to display and manage the player's
level progress in the Turtle Crossing game. Inherits from the Turtle
class to render the level and game over message directly on the
game screen.
"""

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """
    Represents the scoreboard in the Turtle Crossing game.

    Inherits from Turtle to render the player's current level at the
    top left of the screen and display a game over message when the
    player collides with a car.
    """
    def __init__(self):
        """
        Initializes the Scoreboard with the level set to 1, hides the
        turtle cursor, and displays the initial level at the top left
        of the screen.
        """
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.refresh_scoreboard()

    def  refresh_scoreboard(self):
        """
        Clears the current scoreboard display and rewrites the player's
        current level at the top left of the screen.
        """
        self.clear()
        self.goto(-280,260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def point(self):
        """
        Increments the player's level by one and refreshes the
        scoreboard display to reflect the updated level. Called each
        time the player successfully crosses the finish line.
        """
        self.score += 1
        self.refresh_scoreboard()

    def game_over(self):
        """
        Displays a 'GAME OVER' message at the centre of the screen
        when the player collides with a car and the game ends.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


