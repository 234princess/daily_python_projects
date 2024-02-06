#TODO : Extract colors from picture of Hirst painting
import turtle as t
from turtle import Turtle, Screen
import random

paint =Turtle()
t.colormode(255)


import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r =color.rgb.r
    g =color.rgb.g
    b =color.rgb.b
    new_color =(r,g, b)
    rgb_colors.append(new_color)


list_of_colors = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53),(136, 162, 181),(131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), 
 (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81),(228, 176, 164), (128, 29, 33),(179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), 
 (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205)]

def start_position_x():
    paint.pu()
    paint.setx(-250)
    paint.pd()

def start_position_y():
    paint.pu()
    paint.sety(-250)
    paint.pd()

def draw_dot():
    paint.dot(20, random.choice(list_of_colors))
    paint.pu()
    paint.fd(50)
    paint.pd()

def next_line():
    start_position_x()
    paint.setheading(90)
    paint.pu()
    paint.forward(50)
    paint.pd()
    paint.right(90)
    

lines = 9
paint.hideturtle()  
start_position_x()
start_position_y()

while lines > 0:
    for x in range(10):
          draw_dot()
    next_line()
    lines -= 1
   

screen = Screen()
screen.exitonclick()