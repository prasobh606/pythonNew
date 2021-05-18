"""import turtle as t
window = t.Screen();

window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(825)
window.mainloop()"""
from turtle import *
import turtle as t

window = t.Screen()
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)
left_border = -390
right_border = 390
top_border = 290
bottom_border = -290


left_handle = t.Turtle()
left_handle.shape("square")
left_handle.color("red")
left_handle.speed(1)
left_handle.shapesize(5, 1)
left_handle.penup()
left_handle.goto(left_border, 0)

right_handle = t.Turtle()
right_handle.shape("square")
right_handle.color("red")
right_handle.speed(1)
right_handle.shapesize(5, 1)
right_handle.penup()
right_handle.goto(right_border, 0)

ball = t.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(1)
#ball.shapesize(5, 1)
ball.penup()
ball.goto(5, 5)
ball_xdirection = 3
ball_ydirection = 3

game_exit = False


def left_handler_up():
    y = left_handle.ycor()
    left_handle.sety(y + 30)


def left_handler_down():
    y = left_handle.ycor()
    left_handle.sety(y - 30)
    print(left_handle.xcor(), left_handle.ycor())


def right_handler_up():
    yy = right_handle.ycor()
    right_handle.sety(yy + 30)


def right_handler_down():
    yy = right_handle.ycor()
    right_handle.sety(yy - 30)


def exit_game():
     global game_exit
     game_exit = True



window.onkeypress(left_handler_up, "Up")
window.onkeypress(left_handler_down, "Down")

window.onkeypress(right_handler_up, "Right")
window.onkeypress(right_handler_down, "Left")

window.onkeypress(exit_game, "q")
window.listen()

try:
    while not game_exit:

        window.update()


        ball.setx(ball.xcor()+ball_xdirection)

        ball.sety(ball.ycor()+ball_ydirection)

        if ball.ycor() > top_border:
            ball.sety(top_border)
            ball_ydirection = ball_ydirection*-1
        if ball.ycor() < bottom_border:
            ball.sety(bottom_border)
            ball_ydirection = ball_ydirection*-1
        if ball.xcor() > right_border:
            ball.setx(right_border)
            ball_xdirection = ball_xdirection*-1
        if ball.xcor() < left_border:
            ball.setx(left_border)
            ball_xdirection = ball_xdirection*-1

        if ((ball.xcor() > left_border) and (ball.xcor() < (left_border+20))) and ((ball.ycor()<(left_handle.ycor()+40)) and (ball.ycor()>(left_handle.ycor()-40))):
            ball.setx(left_border+20)
            ball_xdirection = ball_xdirection * -1

        if ((ball.xcor() < right_border) and (ball.xcor() > (right_border-40))) and ((ball.ycor()<(right_handle.ycor()+40)) and (ball.ycor()>(right_handle.ycor()-40))):
            ball.setx(right_border-40)
            ball_xdirection = ball_xdirection * -1

finally:
    print("pgm exited")
window.mainloop()
