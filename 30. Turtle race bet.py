from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
start_y_positions = [-70, -40, -10, 20, 50, 80] 

class Turtle_Class:
    def __init__(self, color, y_position):
        self.turtle = Turtle(shape='turtle')
        self.turtle.penup()
        self.turtle.color(color)
        self.turtle.goto(x= -230, y=y_position)

    def run(self):
        self.turtle.forward(random.randint(0,30))

turtles = []

for i, color in enumerate(colors):
    new_turtle = Turtle_Class(color, start_y_positions[i])
    turtles.append(new_turtle)
        
not_at_finish = True
print(user_bet)


while not_at_finish:
    for turtle in turtles:
        turtle.run()

        if turtle.turtle.xcor() > 230:
            not_at_finish = False
            winning_color = turtle.turtle.color()[0]
            if user_bet.lower() == winning_color:
                print(f"You have won the {winning_color} won! ")
            else:
                print(f"You have lost! The {winning_color} won! ")
            break




screen.exitonclick()
