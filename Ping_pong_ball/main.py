from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title("Ping Pong Game")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

 
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() 
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -275:
        # needs to bounce
        ball.bounce_y()
        
    # Detect collision with right and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.point_scored('left')
        # game_is_on= False

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.point_scored('right')
        
        
screen.exitonclick()