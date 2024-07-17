from turtle import Turtle


class DividingLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setheading(90)
        self.color("white")
        self.penup()
        self.goto(x=0, y=-300)
        self.draw_line()

    def draw_line(self):
        while self.ycor() < 300:
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()

