from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

"""
Pong Game - Main Entry Point

A graphical two-player Pong game built with Python's Turtle module where
two players control paddles to deflect a ball and score points when the
opposing player misses the ball.

Process:
    1. Initializes two paddles, a ball, and a scoreboard from their
       respective modules.
    2. Listens for keyboard inputs to control both paddles:
          - Right paddle: Up/Down arrow keys.
          - Left paddle:  'W' key to move up, 'S' key to move down.
    3. Runs the main game loop, updating the screen at the ball's
       current move speed:
          a. Moves the ball one step in its current direction.
          b. Checks for a collision with the top or bottom walls
             and bounces the ball vertically.
          c. Checks for a collision with either paddle (within 50 units)
             and bounces the ball horizontally, increasing its speed
             by 10% with each paddle hit.
          d. Checks if the ball passes the right boundary (x > 380):
             - Resets the ball to the centre.
             - Awards a point to the left player.
          e. Checks if the ball passes the left boundary (x < -380):
             - Resets the ball to the centre.
             - Awards a point to the right player.
    
Game Details:
    Speed:      Screen updates at the ball's move_speed (starting at
                0.1 seconds), decreasing by 5% with each paddle bounce, 
                thus increasing the ball speed.
    Controls:   Right player uses Up/Down arrow keys.
                Left player uses W/S keys.

Dependencies:
    turtle.Screen:        Used to set up the graphical screen, listen for
                          keyboard input, and handle the exit click event.
    paddle.Paddle:        Manages each player's paddle, its position, and
                          up/down movement via paddle_up() and paddle_down().
    ball.Ball:            Manages the ball's movement, bouncing, speed, and
                          position reset via move(), bounce_x(), bounce_y(),
                          and reset_position().
    scoreboard.Scoreboard: Manages the score display and increments each
                           player's score via l_point() and r_point().
    time:                 Used to control the game speed via sleep() delays
                          based on the ball's current move_speed.
"""

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")

#Disable the automatic screen update
screen.tracer(0)

#Right paddle
r_paddle = Paddle((350, 0))
#Leftt paddle
l_paddle = Paddle((-350, 0))
#Ball
ball = Ball()
#Scoreboard
scoreboard = Scoreboard()

#Listen for directions from arrows
screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

game_is_active = True

while game_is_active:
    # Update the screen after the segments have been moved
    screen.update()
    #Set the delay between screen updates
    time.sleep(ball.move_speed) #0.1 seconds at beginning of each point

    # Move the ball in small increments
    ball.move()

    #Check for a collision with top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Check for a collision with left or right paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Right player misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Leftt player misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
