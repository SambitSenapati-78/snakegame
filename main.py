from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game ! ! !")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
# move snake using keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# animating snake segments to move
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    # detect collision with tail
    for segment in snake.snake_tail[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
