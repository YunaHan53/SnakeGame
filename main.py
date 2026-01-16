from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

# Snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.move()
        snake.grow()
        score.scoring()

    # Detect collision with the walls
    current_x_pos = snake.head.xcor()
    current_y_pos = snake.head.ycor()
    if current_x_pos <= -295 or current_y_pos <= -295 or current_x_pos >= 295 or current_y_pos >= 295:
        score.game_over()
        game_is_on = False

    # Detect collision with the tail
    for seg in snake.snake_segments[3:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()