from turtle import Turtle

class State(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x, y)
        self.write(name, font=["Arial", 6, "bold"])

