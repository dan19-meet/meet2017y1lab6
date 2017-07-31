import turtle

'''
turtle.shape('turtle')
square = turtle.clone()
square.shape("square")
square.goto(100, 100)

triangle = square.clone()
triangle.shape("triangle")

triangle.goto(200, 0)
triangle.goto(0, 0)

square.goto(300, 300)
square.stamp()
square.goto(-100, -100)

print(a)
'''

speed = 5

UP = 0
LEFT = 1
DOWN = 3
RIGHT = 4

direction = UP

turtle.hideturtle()
turtle.pensize(10)
turtle.left(90)
turtle.shape("square")


UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"


def up():
    direction = UP
    print(direction)

    oldPos = turtle.pos()
    x, y = oldPos
    
    turtle.goto(x, y + speed)
    print(turtle.pos())

def down():
    direction = DOWN
    print(direction)

    oldPos = turtle.pos()
    x, y = oldPos

    turtle.goto(x, y - speed)
    print(turtle.pos())

def right():
    direction = RIGHT
    print(direction)

    oldPos = turtle.pos()
    x, y = oldPos

    turtle.goto(x + speed, y)
    print(turtle.pos())

def left():
    direction = LEFT
    print(direction)

    oldPos = turtle.pos()
    x, y = oldPos

    turtle.goto(x - speed, y)
    print(turtle.pos())

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(turtle.stamp, SPACEBAR)
turtle.listen()


turtle.mainloop()
