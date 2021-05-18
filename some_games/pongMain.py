import turtle as t


class PongWindow:
    def __init__(self, width, height, color):
        self.window = t.Screen()
        self.window.bgcolor(color)
        self.window.setup(width=width, height=height)
        self.window.tracer(0)
        self.left_border = -390
        self.right_border = 390
        self.top_border = 290
        self.bottom_border = -290
        self.handle_up_move = 20
        self.handle_down_mov = -20
        self.left_handle = None
        self.right_handle = None
        self.ball = None
        self.game_exit = False

    def set_window(self):
        pass

    def main_loop(self):
        self.window.mainloop()

    def int_events(self, left_handle, right_handle):
        self.left_handle = left_handle
        self.right_handle = right_handle

        self.window.onkeypress(self.left_handler_up, "a")
        self.window.onkeypress(self.left_handler_down, "z")

        self.window.onkeypress(self.right_handler_up, "Up")
        self.window.onkeypress(self.right_handler_down, "Down")

        self.window.onkeypress(self.exit_game, "q")

        self.window.listen()

    def left_handler_up(self):
        self.left_handle.set_ycor(self.handle_up_move)


    def left_handler_down(self):
        self.left_handle.set_ycor(self.handle_down_mov)

    def right_handler_up(self):
        self.right_handle.set_ycor(self.handle_up_move)

    def right_handler_down(self):
        self.right_handle.set_ycor(self.handle_down_mov)

    def exit_game(self):
        self.game_exit = True
        print("game exited")


class Handle(PongWindow):
    def __init__(self, position):
        self.position = position
        self.handle = t.Turtle()
        self.handle.shape("square")
        self.handle.color("red")
        self.handle.speed(0)
        self.handle.shapesize(5, 1)
        self.upmove = 20
        self.downmove = -20
        self.cor = {}
        self.handle.penup()
        self.handle.goto(self.position, 0)

        self.cor['y'] = self.handle.ycor()
        self.cor['x'] = self.handle.xcor()

    def make_handle(self):
        pass

    def set_ycor(self, pos):
        y = self.handle.ycor()

        if (y + pos) < -250:
            self.handle.sety(-250)
        elif (y+pos) > 250:
            self.handle.sety(250)
        else:
            self.handle.sety(y + pos)
        self.cor['y'] = self.handle.ycor()
        self.cor['x'] = self.handle.xcor()


class Ball:
    def __init__(self, position):
        self.position = position
        self.ball = t.Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.speed(0)
        # self.ball.shapesize(5, 1)
        self.ball.penup()
        self.ball.goto(self.position, self.position)
        self.ball_xdirection = 3
        self.ball_ydirection = 3
        self.playerA_point = 0
        self.playerB_point = 0
        self.min_point = 10
        self.playerA_point = 0
        self.playerB_point = 0

        self.pen = t.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 310)
        self.pen.write("Player A:0  Player B:0", align="center", font={"Arial", 30, "normal"})

    def set_xcor(self):

        self.ball.setx(self.ball.xcor() + self.ball_xdirection)

        # print(self.ball_xdirection)

    def set_ycor(self):
        # print(self.ball.ycor())
        self.ball.sety(self.ball.ycor() + self.ball_ydirection)

    def check_window_borders(self, left, right, top, bottom, l_handle, r_handle):
        # print(f"left = {left}, right = {right}, top = {top}, bottom = {bottom}")
        if self.ball.ycor() > top:
            self.ball.sety(top)
            self.ball_ydirection = self.ball_ydirection * -1
        if self.ball.ycor() < bottom:
            self.ball.sety(bottom)
            self.ball_ydirection = self.ball_ydirection * -1
        if self.ball.xcor() > right:
            self.ball.setx(right)
            self.ball_xdirection = self.ball_xdirection * -1
            test = self.playerA_point
            self.playerA_point += 1
            self.update_score()

        if self.ball.xcor() < left:
            self.ball.setx(left)
            self.ball_xdirection = self.ball_xdirection * -1
            self.playerB_point += 1
            self.update_score()

        if ((self.ball.xcor() > left) and (self.ball.xcor() < (left + 20))) and (
                self.ball.ycor() < (l_handle['y'] + 60) and (self.ball.ycor() > (l_handle['y'] - 60))):
            self.ball.setx(left + 20)
            self.ball_xdirection = self.ball_xdirection * -1
            # self.playerA_point += self.min_point

        if ((self.ball.xcor() < right) and (self.ball.xcor() > (right - 20))) and (
                (self.ball.ycor() < (r_handle['y'] + 60)) and (self.ball.ycor() > (r_handle['y'] - 60))):
            self.ball.setx(right - 20)
            self.ball_xdirection = self.ball_xdirection * -1
            # self.playerB_point += self.min_point

    def update_score(self):
        self.pen.clear()
        self.pen.write("Player A:{}  Player B:{}".format(self.playerA_point, self.playerB_point), align="center",
                       font={"Arial", 30, "normal"})


class Pane:
    def __init__(self):
        self.p = t.Turtle()
        self.p.shape('square')
        self.p.shapesize(30, 40)
        self.p.color('blue')
        self.p.penup()

pong = PongWindow(900, 700, "green")
Pane()
left_handle = Handle(-390)
right_handle = Handle(390)

pong.int_events(left_handle, right_handle)
ball = Ball(5)






# while (not pong.game_exit) or ((ball.playerA_gameOut > 1) or (ball.playerB_gameOut > 1)):
# while (not pong.game_exit) and ((ball.playerA_gameOut > 0) and (ball.playerB_gameOut > 0)):
while not pong.game_exit:
    ball.set_xcor()
    ball.set_ycor()
    """ 
    game_out_in = ball.playerA_point if (ball.playerA_point < ball.playerB_point) else ball.playerB_point

   
    current_game.mark_point(game_out_in)
    current_game.reset_pen()
    current_game.mark_point(game_out_in)
    """
    ball.check_window_borders(-390, 390, 290, -290, left_handle.cor, right_handle.cor)
    # print(ball.playerA_gameOut, ball.playerB_gameOut)
    pong.window.update()

print(ball.playerA_point)
print(ball.playerB_point)
pong.main_loop()
# pong.main_loop()
