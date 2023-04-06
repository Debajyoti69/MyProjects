import turtle
import time

tim = turtle.Turtle()

screen = turtle.Screen()
screen.tracer(0)
screen.title("PONG")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fast")
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# screen.getcanvas().bind("<Up>", r_paddle.go_up)
# screen.onkey(r_paddle.go_up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detection with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # restart if paddle misses the ball
    if ball.xcor() > 380:  # or ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
