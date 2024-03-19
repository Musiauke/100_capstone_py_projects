import turtle as t
import random

rgb = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (217, 88, 51)]

# the image should be 10 x 10 dots 

screen = t.Screen()
tim = t.Turtle()

screen.bgcolor("white")
screen.setup(width=1000,height=1000)
tim.hideturtle()
tim.penup()
tim.goto(-300,300)


def paint_dots():
    for _ in range(10):
        color = random.choice(rgb)
        color_normalized = (color[0]/255, color[1]/255, color[2]/255)
        tim.color(color_normalized)
        tim.dot(20)
        tim.forward(40)


def paint_square():
    for _ in range(10):
        paint_dots()
        x = tim.xcor()
        y = tim.ycor()
        tim.goto(x - 400, y-40)

paint_square()


screen = t.Screen()
screen.exitonclick()

