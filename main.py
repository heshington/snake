
from turtle import Screen
import time
screen = Screen()
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sssssnnnaaaakkeee")
screen.tracer(0)

loop_lambda = lambda: loop(repeat=False)
snake = Snake(loop_lambda)
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def loop(repeat=True):
    screen.update()
    snake.move()

    #Detech collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # # Detech collision with wall.
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     scoreboard.game_over()
    #     return

    # Detech collision with wall.
    if snake.head.xcor() > 300:
        snake.head.setx(snake.head.xcor() - 300*2)
    if snake.head.xcor() < -300:
        snake.head.setx(snake.head.xcor() + 300 * 2)
    if snake.head.ycor() > 300:
        snake.head.sety(snake.head.ycor() - 300 * 2)
    if snake.head.ycor() < -300:
        snake.head.sety(snake.head.ycor() + 300 * 2)

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            scoreboard.game_over()
            return

    if repeat:
        screen.ontimer(loop, 100)


# screen.exitonclick()
screen.ontimer(loop, 2000)
screen.mainloop()
