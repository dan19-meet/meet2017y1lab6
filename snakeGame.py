import turtle

speed = 2.5
global angleOfTurtle

turtle.pensize(5)
turtle.hideturtle()
turtle.shape("square")

def moveUp():
    if angleOfTurtle == 0:
        turtle.left(90)
    elif angleOfTurtle == 180:
        turtle.right(90)
        
def moveRight():
    turtle.right(90)

def moveLeft():
    turtle.left(90)

def keyPressed():
    turtle.onkeypress(moveUp, 'w')
    turtle.onkeypress(moveLeft, 'a')
    turtle.onkeypress(moveRight, 'd')
    turtle.listen()

while True:
    angleOfTurtle = turtle.heading()
    keyPressed()
    turtle.forward(speed)

turtle.mainloop()
