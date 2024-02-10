import time

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


turtle_player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun=turtle_player.move_up, key="Up")

 
#TODO:Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    #TODO:Detect when the turtle player collides with a car and stop the game if this happens.
    for car in cars.all_cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #TODO:Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).      
    if turtle_player.at_finish_line():
        turtle_player.go_to_start()
        cars.level_up()
        scoreboard.increase_level()
    


screen.exitonclick()