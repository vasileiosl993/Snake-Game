from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Quiz")
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
    snake.move_snake()
    screen.update()
    time.sleep(0.1)

    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    if snake.snakes[0].xcor() > 280 or snake.snakes[0].ycor() > 290 or snake.snakes[0].xcor() < -300 or snake.snakes[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snakes:
        if segment == snake.snakes[0]:
            pass
        elif snake.snakes[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
