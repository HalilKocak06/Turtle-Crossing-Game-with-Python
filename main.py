from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600 , 600)
screen.bgcolor("white")
screen.tracer(0)


Player1=Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(Player1.move ,"Up" )



game_is_on =True

while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move_cars()

    if Player1.ycor() > 290 :
        Player1.reset_position()
        scoreboard.increase_level()
        car_manager.level_up()


    #TODO 1:Yüksek levellarda arabalar kaza yapmıyor örnek lvl5
    for car in car_manager.all_cars:
        if car.distance(Player1) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()