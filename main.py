from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time


# This file runs the main game loop.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake.py")
screen.tracer(0)

# Objects are created from the class files with reasonable names.
# One class per file as of now because brevity
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# These functions just listen for key presses and then runs functions from snake class if pressed
# For movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -300:
        scoreboard.game_over()
        game_is_on = False

    # if head collides with segment in tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

# This must be after everything else! Makes just screen doesn't quit before it's clicked
# without this it just flashes once
screen.exitonclick()

