from turtle import Turtle

class Paddle:
    def __init__(self, x):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.setx(x)
        self.paddle.sety(0)

    def up(self):
        pos = self.paddle.ycor() + 20
        self.paddle.sety(pos)

    def down(self):
        pos = self.paddle.ycor() - 20
        self.paddle.sety(pos)