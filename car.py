from turtle import Turtle
import random 

class Car(Turtle):

    #(width= 800, height=600)
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3) 
        self.color(self.random_color())  
        self.penup()
        random_y = random.randint(-600,600)
        self.goto(400, random_y)

    @staticmethod
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    
        return (r, g, b)


    def go_left(self, speed):
        new_x = self.xcor() - speed
        self.goto(new_x, self.ycor())

  
