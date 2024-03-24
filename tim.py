from turtle import Turtle

class Tim(Turtle):

    def __init__(self, level):
        super().__init__()
        self.shape("turtle")
        self.color(0,0,0)  
        self.penup()
        self.goto(0,-200)   

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y) 

class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align="center", font=("Courier", 24, 'normal'))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, 'normal'))