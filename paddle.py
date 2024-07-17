from turtle import Turtle

MOVE_DISTANCE = 60


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1, outline=1)
        self.goto(x_cor, 0)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y <= 250:  # Ensure paddle stays within screen boundaries
            self.sety(new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y >= -240:  # Ensure paddle stays within screen boundaries
            self.sety(new_y)
