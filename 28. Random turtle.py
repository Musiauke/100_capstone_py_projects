import turtle as t
import random

tim = t.Turtle()
tim.shape('turtle')
t.colormode(1.0) 

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b) 
for _ in range(250): 
    random_angle = random.randint(0, 360) 
    random_forward = random.randint(10, 50)  
    right_or_left = random.choice([tim.right, tim.left])  
    random_speed = random.randint(1,50)
    tim.color(random_color()) 
    tim.forward(random_forward)
    right_or_left(random_angle)  
    tim.speed(random_speed)

screen = t.Screen()
screen.exitonclick()
