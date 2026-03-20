from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

"""
Snake Game - Main Entry Point (with High Score Tracking)

A graphical Snake game built with Python's Turtle module where the player
controls a growing snake, collecting food while avoiding walls and its
own tail. Highest score is tracked and the snake is reset after a collision.

Process:
    1.  Initializes the snake, food, and scoreboard from their respective
       modules.
    2. Listens for arrow key inputs to control the snake's direction.
    4. Runs the main game loop, updating the screen every 0.1 seconds:
          a. Moves the snake forward one step in its current direction.
          b. Refreshes the scoreboard display.
          c. Checks for a collision with food :
             - Repositions the food randomly on the screen.
             - Extends the snake's length by one segment.
             - Increments and refreshes the scoreboard.
          d. Checks for a collision with the wall boundaries or with the snake's own tail segments:
             - Resets the current score, updating the high score
               if the current score exceeds it.
             - Resets the snake to its starting position and length.
 
Game Details:
    Speed:      Screen updates every 0.1 seconds per game loop iteration.
    Food:       Randomly repositioned each time the snake collects it.
    Scoring:    Current score increments with each food collected.
                Highest score is stored in a file and preserved.

Dependencies:
    turtle.Screen:         Used to set up the graphical screen, listen for
                           keyboard input, and handle the exit click event.
    time:                  Used to control the game speed via sleep() delays.
    food.Food:             Manages the food object and its random
                           repositioning via refresh().
    snake.Snake:           Manages the snake's segments, movement, direction
                           controls, extension, and reset via move(),
                           extend(), reset_snake(), snake_up(), snake_down(),
                           snake_left(), and snake_right().
    scoreboard.Scoreboard: Manages the score display, increments the score,
                           tracks the highest score, and resets the current
                           score via update_scoreboard() and reset_score().
"""

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
#Disable the automatic screen update
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Listen for directions from arrows
screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")

game_is_active = True

while game_is_active:
    # Update the screen after the segments have been moved
    screen.update()
    #Set the delay between screen updates
    time.sleep(0.1) #0.1 seconds
    snake.move()
    scoreboard.update_scoreboard()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.update_scoreboard()

    #Detect a collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    #Detect a collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()

