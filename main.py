# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates
# Day 21 - Intermediate - Build the Snake Game Part 2: Class Inheritance & Slicing List and Dictionaries
# Day 25 - Intermediate - Files, Directories and Paths, added high score (Oct-14-2024)

# Improvements and bugs:
# 1. Improvement: When snake collides instead of restarting right away, freeze the frame, add an option to press a key to restart or press another key to quite.
# 2. After collision snake should for example freeze and blink to indicate that a collision had happened.
# 3. Enter a name at the start, create a list of highest scores with names.

from turtle import Screen
from food import Food
from scoreboard import Scoreboard
# from button import Button # for cellphone use
from snake import Snake
import time

WALL_LOCATION = 300 # Used for collision detection with snake's head

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turn off turtle animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# # For cellphone use, test, not working, yet
# button = Button(text="up", location=(15, 15), onclick_action=snake.up)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # adds 0.1 second delay, basically sets FPS
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    # Detect collision with wall.
    if snake.head.xcor() > WALL_LOCATION or snake.head.xcor() < -WALL_LOCATION or snake.head.ycor() > WALL_LOCATION or snake.head.ycor() < -WALL_LOCATION:
        # game_is_on = False # Day 25 - Oct-14-2024 - high score, commented out
        # scoreboard.game_over() # Day 25 - Oct-14-2024 - high score, commented out, scoreboard.reset() is used instead
        scoreboard.reset_snake() # Day 25 - Oct-14-2024 - high score
        snake.reset_snake() # Day 25 - Oct-14-2024 - high score

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False # Day 25 - Oct-14-2024 - high score, commented out
            # scoreboard.game_over() # Day 25 - Oct-14-2024 - high score, commented out, scoreboard.reset() is used instead
            scoreboard.reset_snake() # Day 25 - Oct-14-2024 - high score
            snake.reset_snake()  # Day 25 - Oct-14-2024 - high score

screen.exitonclick()
