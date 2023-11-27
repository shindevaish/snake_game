import turtle as tt
import random as rand
import time

#setting screen
screen=tt.Screen()
screen.bgcolor("Black")
screen.setup(width=600,height=600)
screen.title("SNAKE GAME")

#mouth of snake
mouth=tt.Turtle()
mouth.shape("square")
mouth.color("white")
mouth.penup()
mouth.goto(0,0)
mouth.speed(5)
mouth.direction = "stop"

#food for snake
food=tt.Turtle()
food.speed(0)
food.penup()
food.shape("circle")
food.color("green")
food.goto(rand.randint(-290,290),rand.randint(-290,290))

#snake movement in different direction
def snakeup():
    if mouth.direction != "down":
        mouth.direction="up"
        y=mouth.ycor()
        mouth.sety(y+20)
        if mouth.ycor()>295:
            mouth.sety(y)

def snakedown():
    if mouth.direction != "Up":
        mouth.direction="Down"
        y=mouth.ycor()
        mouth.sety(y-20)
        if mouth.ycor()<-295:
            mouth.sety(y)


def snakeright():
    if mouth.direction != "Left":
        mouth.direction="Right"
        x=mouth.xcor()
        mouth.setx(x+20)
        if mouth.xcor()>295:
            mouth.setx(x)

def snakeleft():
    if mouth.direction != "Right":
        mouth.direction="Left"
        x=mouth.xcor()
        mouth.setx(x-20)
        if mouth.xcor()>-295:
            mouth.sety(x)

screen.listen()
screen.onkeypress(snakeup,"Up")
screen.onkeypress(snakedown,"Down")
screen.onkeypress(snakeleft,"Left")
screen.onkeypress(snakeright,"Right")

nwbody=[]
while True:
    screen.update()

    if mouth.ycor()<295 or mouth.ycor()>-295 or mouth.xcor()<295 or mouth.ycor()>-295 :
        time.sleep(1)
        mouth.goto(0,0)
        mouth.direction="stop"

    if mouth.distance(food)<20:
        food.goto(rand.randint(-285,285),rand.randint(-285,285))

        body=tt.Turtle()
        body.shape("square")
        body.color("red")
        body.penup()
        nwbody.append(body)

        for i in range(0,len(nwbody)):
            x=mouth.xcor()
            y=mouth.ycor()
            nwbody[i].setx(x+i*20)
            nwbody[i].sety(y+i*20)
            
turtle.done()
