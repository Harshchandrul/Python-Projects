from turtle import  Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()
    
screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_forward()
    
    # detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.ycor() > 270:
        scoreboard.level_up()
        cars.increase_speed()
        player.position_reset()

screen.exitonclick()