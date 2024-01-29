#import practice_module
#print(practice_module.number)

#from practice_module import number
#print(number)

#import turtle
#timi = turtle.Turtle()

#from turtle import Turtle,Screen
#timy = Turtle()
#print(timy)
#timy.shape("turtle")
#timy.color('red')
#timy.forward(100)

#screen = Screen()
#print(screen.canvheight)
#print(screen.exitonclick())

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print (table)