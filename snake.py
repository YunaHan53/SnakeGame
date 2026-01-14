from turtle import Turtle
STARTING_POSITION = {(0, 0), (-20, 0), (-40, 0)}
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_seg = Turtle("square")
        new_snake_seg.goto(position)
        new_snake_seg.color("white")
        new_snake_seg.penup()
        self.snake_segments.append(new_snake_seg)

    def grow(self):
        """Adds a new segment to the snake"""
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        """Sets the movement of each snake segment to the position of the segment before following the snake head."""
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            x = self.snake_segments[seg_num - 1].xcor()
            y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x, y)
        self.snake_segments[0].forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)