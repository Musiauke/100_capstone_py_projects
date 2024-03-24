from turtle import Screen
from tim import Tim, Scoreboard
from car import Car
import random

screen = Screen()
screen.colormode(255)
screen.setup(width= 800, height=600)
screen.bgcolor("white")
screen.title('Turtle crossing the street')
screen.tracer(0)

tim = Tim(level=1)
cars = []
car_speed = 10
level = 1
scoreboard = Scoreboard(level)

def create_car():  
    if random.randint(1, 5) == 1:
        cars.append(Car())

def move_cars():
    for car in cars:
        car.go_left(car_speed)

        if car.xcor() < -420:
            car.hideturtle()
            cars.remove(car)

def check_collision():
    for car in cars:
        if tim.distance(car) < 20:
            print("You have colided with the car! ")
            scoreboard.game_over()
            global game_is_on
            game_is_on = False
            return
        
def game_loop():
    if game_is_on:
            create_car()
            move_cars()
            check_collision() 
            check_level_up()
            screen.update()
            screen.ontimer(game_loop, 100)

def check_level_up():
    if tim.ycor() > 280:
        tim.goto(0, -280)  
        scoreboard.increase_level()
        global car_speed
        car_speed *= 1.1



game_is_on = True

screen.listen()
screen.onkey(tim.go_up, 'Up')

if game_is_on:
    game_loop()
else:
    screen.bye()
    




screen.exitonclick()