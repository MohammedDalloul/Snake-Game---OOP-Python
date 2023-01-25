from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Mohammed Snake-Game")
screen.tracer(0)

my_snake = Snake()


screen.listen()
screen.onkey(fun=my_snake.up, key="Up")
screen.onkey(fun=my_snake.down, key="Down")
screen.onkey(fun=my_snake.turn_rt, key="Right")
screen.onkey(fun=my_snake.turn_lt, key="Left")

food = Food()

score = Scoreboard()


game_over = False
while not game_over:
    screen.update()
    time.sleep(0.09)
    my_snake.move()


    if my_snake.snakes_st[0].distance(food) < 13:
        my_snake.extend_snake()
        food.change_place()
        score.increase_score()


    if my_snake.snakes_st[0].xcor() > 380 or my_snake.snakes_st[0].xcor() < -380 or my_snake.snakes_st[0].ycor() > 280 or my_snake.snakes_st[0].ycor() < -280:
        score.restart_game()
        my_snake.reset_snake()

    for segment in my_snake.snakes_st[1:]:
        if my_snake.snakes_st[0].distance(segment) < 10:
            score.restart_game()

            my_snake.reset_snake()


screen.exitonclick()