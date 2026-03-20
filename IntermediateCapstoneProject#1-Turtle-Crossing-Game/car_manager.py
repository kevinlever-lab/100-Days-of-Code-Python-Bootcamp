from turtle import Turtle
import random

"""
Car Manager Module

Defines the CarManager class used to create and manage all cars in the
Turtle Crossing game. Handles car spawning, movement, and speed increases
as the player advances through levels.
"""

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    """
        Manages the creation, movement, and speed of all cars in the
        Turtle Crossing game.

        Cars are randomly spawned on the right side of the screen and move
        left across the screen. The speed of all cars increases each time
        the player successfully crosses the finish line.

        Attributes:
            car_list (list): A list of Turtle objects representing all active
                             cars currently on the screen.
            speed (int):     The current movement distance per game loop step
                             for all cars, starting at STARTING_MOVE_DISTANCE
                             and increasing by MOVE_INCREMENT with each level.
        """

    def __init__(self):
        """
        Initializes the CarManager with an empty car list and sets the
        starting movement speed to STARTING_MOVE_DISTANCE (5 units).
        """
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        #Create a new car based on randon 1 in 6 chance
        """
        Randomly spawns a new car on the right side of the screen with
        a 1 in 6 chance per game loop iteration. Each car is a randomly
        coloured rectangle positioned at x = 300 with a randomly
        generated y coordinate between -250 and 250, moving left
        across the screen.
        """
        random_new_car = random.randint(1,6)
        if random_new_car ==1:
            # Car is rectangle 40x20
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            # X position is constant. Y position is randomly generated with a safety margin of 50px
            x_position = 300
            random_y = random.randint(-250, 250)
            # Randomly select colour from the list
            new_car.goto(x_position, random_y)
            # Randomly select colour from the list
            new_car.color(random.choice(COLORS))
            self.car_list.append(new_car)

    def move_cars(self):
        """
        Moves all active cars in the car list forward by the current
        speed value, advancing each car from right to left across
        the screen.
        """
        for car_object in self.car_list:
            car_object.forward(self.speed)

    def accelerate(self):
        """
        Increases the movement speed of all cars by MOVE_INCREMENT
        (10 units) each time the player successfully crosses the
        finish line, making each level progressively more difficult.
        """
        self.speed += MOVE_INCREMENT