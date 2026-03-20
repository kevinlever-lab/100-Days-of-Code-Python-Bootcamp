from turtle import Turtle

"""
Snake Module (with Reset Functionality)

Defines the Snake class used to create and manage the snake in the Snake
game. Handles the snake's creation, movement, growth, directional controls,
and reset functionality when a collision is detected. This version extends
the original Snake class with a reset_snake() method that resets the snake
to its starting position and length without ending the game.
"""

# Constant to store the starting position for the first three segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    """
    Represents the snake in the Snake game.

    Manages the snake's body segments, controls its movement across the
    screen, handles directional input from the player, extends the snake's
    length when food is collected, and resets the snake to its starting
    state when a collision with a wall or tail is detected.
    """
    def __init__(self):
        """
        Initializes the Snake with three starting segments at the
        predefined starting positions and sets the head to the
        first segment.
        """
        # List to store segment objects (Turtle objects)
        self.segments = []
        # Starting position for the first three segments
        self.create_snake()
        self.head = self.segments[0]

    # Create the initial three segments and append to the segments list
    def create_snake(self):
        """
        Creates the initial three body segments of the snake at the
        predefined starting positions and appends them to the
        segments list.
        """
        for position in STARTING_POSITIONS :
           self.add_segment(position)

    def add_segment(self, position):
        """
        Creates a new white square Turtle segment at the given position
        and appends it to the segments list.
        """
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """
        Extends the snake by adding a new segment at the position of
        the last segment in the segments list, growing the snake's
        length by one when food is collected.
        """
        #Add the last segment to the list of segments
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        """
        Resets the snake to its initial state after a collision with
        a wall or the snake's own tail.
        """
        #Move existing snake segments off the screen before clearing existing snake segments
        for seg in self.segments:
            seg.goto(1000, 1000)
        #Clear all existing snake segments
        self.segments.clear()
        #Create the initial three segments and append to the segments list
        self.create_snake()
        self.head = self.segments[0]


    def move(self):
        """
        Moves the snake forward by one step. Each body segment moves
        to the position of the segment ahead of it, starting from the
        tail, and the head advances forward by MOVE_DISTANCE units.
        """
        # Lists start counting from 0, so last position is length of list - 1
        # range(start, stop, step)
        for segment_num in range(len(self.segments) - 1, 0, -1):
            # Set the position of the segment to equal the position of the preceding segment, starting with the very
            # last segment and finishing at the second segment
            # Update the coordinates in the segments list
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)

        #move first segment - head of the snake
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        """
        Turns the snake upward. Only applies if the snake is currently
        heading east (0°) or west (180°) to prevent reversing direction.
        """
        snake_heading = self.head.heading()
        # Ignore direction if heading north or south
        if snake_heading == 0:
            self.head.left(90)
        elif snake_heading == 180:
            self.head.right(90)

    def snake_down(self):
        """
        Turns the snake downward. Only applies if the snake is currently
        heading east (0°) or west (180°) to prevent reversing direction.
        """
        snake_heading = self.head.heading()
        # Ignore direction if heading north or south
        if snake_heading == 0:
            self.head.right(90)
        elif snake_heading == 180:
            self.head.left(90)

    def snake_left(self):
        """
        Turns the snake left. Only applies if the snake is currently
        heading north (90°) or south (270°) to prevent reversing direction.
        """
        snake_heading = self.head.heading()
        # Ignore direction if heading east or west
        if snake_heading == 90:
            self.head.left(90)
        elif snake_heading == 270:
            self.head.right(90)

    def snake_right(self):
        """
        Turns the snake right. Only applies if the snake is currently
        heading north (90°) or south (270°) to prevent reversing direction.
        """
        snake_heading = self.head.heading()
        # Ignore direction if heading east or west
        if snake_heading == 90:
            self.head.right(90)
        elif snake_heading == 270:
            self.head.left(90)
