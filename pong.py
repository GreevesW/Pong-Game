import turtle as t
import os

PlayerAscore = 0
PlayerBscore = 0

window = t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#creating left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=0.2)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=0.2)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

#creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.goto(0,260)
pen.write("score",align="center",font=("Arial",24,"normal"))


#moving the leftpaddle

def leftpaddleup():
  y = leftpaddle.ycor()
  y = y+90
  leftpaddle.sety(y)
  
def leftpaddledown():
  y = leftpaddle.ycor()
  y = y-90
  leftpaddle.sety(y)
  
#moving the rightpaddle
def rightpaddleup():
  y = rightpaddle.ycor()
  y = y+90
  rightpaddle.sety(y)
  
def rightpaddledown():
  y = rightpaddle.ycor()
  y = y-90
  rightpaddle.sety(y)

#assign keys to play
window.listen()
window.onkeypress(leftpaddleup,"w")
window.onkeypress(leftpaddledown,"s")
window.onkeypress(rightpaddleup,"Up")
window.onkeypress(rightpaddledown,"Down")

#main game loop
while True:
  window.update()

  #moving the ball
  ball.setx(ball.xcor()+ballxdirection)
  ball.sety(ball.ycor()+ballydirection)

  #setting up border
  if ball.ycor()>290:
    ball.sety(290)
    ballydirection=ballydirection*-1
  if ball.ycor()<-290:
    ball.sety(-290)
    ballydirection=ballydirection*-1

  if ball.xcor() > 390:
    ball.goto(0,0)
    ballxdirection=ballxdirection
    PlayerAscore=PlayerAscore +1
    pen.clear()
    pen.write("player A:{}   player B:{}".format(PlayerAscore,PlayerBscore),align="center")

  if ball.xcor() < -390:
    ball.goto(0,0)
    ballxdirection=ballxdirection
    PlayerBscore=PlayerBscore +1
    pen.clear()
    pen.write("player A:{}   player B:{}".format(PlayerAscore,PlayerBscore),align="center")

#collisions
  if(ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightpaddle.ycor()+50 and ball.ycor()>rightpaddle.ycor()-50):
    ball.setx(340)
    ballxdirection=ballxdirection*-1
    
  if(ball.xcor()<-340)and(ball.xcor()>-350)and(ball.ycor()<leftpaddle.ycor()+50 and ball.ycor()>leftpaddle.ycor()-50):
    ball.setx(-340)
    ballxdirection=ballxdirection*-1