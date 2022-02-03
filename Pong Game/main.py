from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title('Pong')
screen.tracer(0)


l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()




screen.listen()
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')


score = Scoreboard()



while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect right paddle misses
    if ball.xcor() > 380: 
        ball.reset_position()
        score.l_point()
        
    #Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()