from turtle import Turtle, Screen

titi = Turtle()
screen = Screen()


def move_forward():
    titi.fd(20)

def move_backward():
    titi.bk(20)


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
#screen.onkey(key="a", fun=move)
#screen.onkey(key="d", fun=move)
#screen.onkey(key="c", fun=move)

screen.exitonclick()

