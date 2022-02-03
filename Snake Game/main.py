from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

all_turtles = []
score = 0

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

snake = Snake()
food = Food()
score = Scoreboard()



screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.increase_snake()
        food.refresh()
    
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    #Detect collision with tail
    for index in range(1, len(snake.all_turtles)):
        if snake.head.distance(snake.all_turtles[index]) < 10:
            snake.red_color()
            score.game_over()
            game_is_on = False
    
    
screen.exitonclick()

