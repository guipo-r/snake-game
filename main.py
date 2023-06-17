# Imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, GameOver
import time


# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')  # Background color
screen.title("Viborita")
screen.tracer(0)

# Object creation
snake = Snake()
food = Food()
score_board = Scoreboard()
game_is_over = GameOver()

# Keyboard config
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Snake movement
game_is_on = True

while game_is_on:
    screen.update()

    time.sleep(0.15)  # Delay in animation
    snake.move()  # Calling move() function to move forward

    # Detect collision with food and relocate food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.add_square()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        game_is_over.game_over()

    # Detect collision with own body
    for item in snake.squares[2:]:  # Beacuse I want it to skip the neck too
        if snake.head.distance(item) < 10:
            game_is_on = False
            game_is_over.game_over()

screen.exitonclick()
