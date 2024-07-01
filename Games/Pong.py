#Pong game 
import turtle #no need to install extension to run it :)
turtle.speed(0)
window = turtle.Screen()
window.title("Pong by @HeitorSylvester")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(2, 9999)

# Score
score_a = 0 
score_b = 0

# bar 1
bar1 = turtle.Turtle()
bar1.speed (0) #speed animation MAX SPEED (not the bar's speed)
bar1.shape ("square")
bar1.color ("white")
bar1.shapesize(stretch_wid=3, stretch_len=0.5)
bar1.penup()
bar1.goto(-350, 0)

# bar 2 
bar2 = turtle.Turtle()
bar2.speed (0) #speed animation MAX SPEED (not the bar's speed)
bar2.shape ("square")
bar2.color ("white")
bar2.shapesize(stretch_wid=3, stretch_len=0.5)
bar2.penup()
bar2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed (0) #speed animation MAX SPEED (not the bar's speed)
ball.shape ("square")
ball.color ("white")
ball.penup()
ball.goto(0, 0)
ball.dx =  0.5
ball.dy =  0.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("dogica", 15, "bold"))

#function
def bar_1_up():
    y = bar1.ycor()
    y += 50
    bar1.sety(y)

def bar_1_down():
    y = bar1.ycor()
    y -= 50
    bar1.sety(y)

def bar_2_up():
    y = bar2.ycor()
    y += 50
    bar2.sety(y)

def bar_2_down():
    y = bar2.ycor()
    y -= 50
    bar2.sety(y)

#keyboard binding
window.listen()

#bar 1 commands
window.onkeypress(bar_1_up, "w")
window.onkeypress(bar_1_down, "s")

#bar 2 commands
window.onkeypress(bar_2_up, "Up")
window.onkeypress(bar_2_down, "Down")

#Main game loop
while True: 
    turtle.speed(10)
    window.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("dogica", 15, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("dogica", 15, "bold"))

    #Bar and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()< bar2.ycor() + 40 and ball.ycor () > bar2.ycor() -40 ) :
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()< bar1.ycor() + 40 and ball.ycor () > bar1.ycor() -40 ) :
        ball.setx(-340)
        ball.dx *= -1   