from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake=Snake()
food=Food()
screen.listen()
score=Scoreboard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


is_game_play=True

while is_game_play:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_game_play=False
        score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_play = False
            score.game_over()


screen.exitonclick()
