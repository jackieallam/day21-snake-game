from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290\
            or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    tail = snake.segments[1:]   # Slice head off snake
    for seg in tail:
        if snake.head.distance(seg) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
