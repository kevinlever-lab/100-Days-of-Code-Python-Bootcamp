import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

"""
Turtle Crossing Game - Main Entry Point

A graphical arcade game built with Python's Turtle module where the player
controls a turtle attempting to cross a busy road filled with oncoming cars
without being hit, advancing through levels as each crossing is completed.

Process:
    1. Listens for the Up arrow key to move the player turtle forward.
    2. Runs the main game loop, updating the screen every 0.1 seconds:
          a. Spawns new cars randomly on the right side of the screen.
          b. Moves all existing cars from right to left across the screen.
          c. Checks for a collision between the player and any car
             (within 20 units):
             - Ends the game and displays the game over message.
          d. Checks if the player has reached the finish line at the
             top of the screen:
             - Returns the player to the starting position.
             - Increases the speed of all cars.
             - Increments and updates the scoreboard level.

Game Details:
    Speed:      Screen updates every 0.1 seconds per game loop iteration.
    Collision:  Game ends if the player comes within 20 units of any car.
    Levels:     Each time the player crosses the finish line, the car
                speed increases and the level counter increments.
    Controls:   Up arrow key moves the player turtle forward toward the
                finish line. The turtle cannot move backwards or sideways.

Dependencies:
    turtle.Screen:      Used to set up the graphical screen, listen for
                        keyboard input, and handle the exit click event.
    player.Player:      Manages the player turtle's position, upward
                        movement via move_up(), finish line detection via
                        reached_finish_line(), and starting position reset
                        via goto_start().
    car_manager.CarManager: Manages car creation via new_car(), car movement
                            via move_cars(), and speed increases via
                            accelerate(). Maintains the list of all active
                            cars in car_list.
    scoreboard.Scoreboard:  Manages the level display, increments the level
                            via point(), and displays the game over message
                            via game_over().
    time:               Used to control the game speed via sleep() delays.
"""

screen = Screen()
screen.setup(width=600, height=600)
#Disable the automatic screen update
screen.tracer(0)

#Create player object
player = Player()
#Create a car object
car_manager = CarManager()
#Create a scoreboard object
scoreboard = Scoreboard()

#Listen for directions from the keyboard (up arrow) for the turtle's movement
#Turtle can only move up, not backwards or sideways
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    #Schedule screen updates every 0.1s
    #Any changes within this while loop will be refreshed every 0.1s
    time.sleep(0.1)
    screen.update()

    #Create a new car
    car_manager.new_car()
    #Move all cars
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect when the turtle reaches the finish line
    if player.reached_finish_line():
        #Return player to starting position
        player.goto_start()
        #Incease the speed of the cars
        car_manager.accelerate()
        #Update scoreboard
        scoreboard.point()

screen.exitonclick()

