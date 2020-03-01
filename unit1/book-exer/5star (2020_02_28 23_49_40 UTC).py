import turtle 
wn=turtle.Screen()
t=turtle.Turtle()
t.speed(10)

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

def move(t):
    t.forward(350)
    t.right(144)

t.penup()
t.goto(-175,10)
t.pendown()

for i in range (5):
    drawFivePointStar(t)
    move(t)