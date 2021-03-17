from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle1 = Paddle(350)
paddle2 = Paddle(-350)

screen.onkey(key="Up", fun=paddle1.up)
screen.onkey(key="Down", fun=paddle1.down)
screen.onkey(key="w", fun=paddle2.up)
screen.onkey(key="s", fun=paddle2.down)

is_on = True

while is_on:
    screen.update()

screen.exitonclick()