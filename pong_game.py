from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


#TODO: Create the screen
screen = Screen()
screen.title("m's pong game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)


#TODO: configure paddle movement and location
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))

ball = Ball()

l_scoreboard = Scoreboard()
r_scoreboard = Scoreboard()

screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")

screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")



#TODO: starting up game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed())
    screen.update()
    ball.move()

    #TODO:Detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #TODO:Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    #TODO:Detect is ball is out of  bounds on right side
    if ball.xcor() > 380 :
        ball.reset_position()
        l_scoreboard.l_point()
    
    #TODO:Detect is ball is out of  bounds on left side
    if ball.xcor() < -380:
        ball.reset_position()
        r_scoreboard.r_point()



screen.exitonclick()


