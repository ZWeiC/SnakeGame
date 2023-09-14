from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

speed = 2
score = Score()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Snake")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(1 / speed)
    snake.snake_move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.increase_snake()
        score.increase_score()
        speed += 1

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10 :
            is_game_on = False
            score.game_over()




screen.exitonclick()
