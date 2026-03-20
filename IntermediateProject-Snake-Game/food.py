from turtle import Turtle
import random
"""
Food Module

Defines the Food class used to represent the food object in the Snake
game. Inherits from the Turtle class to create and manage a small blue
circular food item that randomly repositions itself on the screen each
time it is collected by the snake.
"""

class Food(Turtle):
    """
    Represents the food object in the Snake game.
    """
    def __init__(self):
        """
        Initializes the Food object as a small blue circle and places
        it at a random position within the game boundaries on the screen.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Repositions the food object to a new random location within
        the game boundaries.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

