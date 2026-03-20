from turtle import Turtle
"""
Scoreboard Module (with Persistent High Score)

Defines the Scoreboard class used to display and manage the score and
high score in the Snake game. Inherits from the Turtle class to render
scores directly on the game screen. Persistent high score tracking by reading and writing
the high score to a data file between game sessions.
"""
#Conatants to store scoreboard configuration
ALIGN = 'center'
FONT = ('Arial', 18, 'normal')
DATAFILE = "data.txt"

class Scoreboard(Turtle):
    """
    Represents the scoreboard in the Snake game with persistent high
    score tracking.

    Inherits from Turtle to render the player's current score and all-time
    high score at the top of the screen. The high score is read
    from and written to a data file, preserving it between game sessions.
    """
    def __init__(self):
        """
        Initializes the Scoreboard, reads the high score from the data
        file, positions the display at the top centre of the screen,
        and renders the initial scoreboard.
        """
        super().__init__()
        self.message = ""
        self.color("white")
        #self.penup()
        #Note, setpos() didn't need penup() to prevent line from being drawn
        self.setpos(0, 270)
        self.score =0
        #Read High score from data file
        with open(DATAFILE) as file:
            self.high_score = int(file.read())
        #Hide the turtle arrow
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        """
        Clears the current scoreboard display and rewrites the player's
        current score and high score at the top centre of the screen.
        """
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def reset_score(self):
        """
        Resets the current score to zero after a collision. If the
        current score exceeds the high score, the high score is updated
        and written to the data file for persistence between sessions.
        The scoreboard is refreshed to reflect the updated scores.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            #Write high_score to data.txt file
            with open(DATAFILE, mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()






