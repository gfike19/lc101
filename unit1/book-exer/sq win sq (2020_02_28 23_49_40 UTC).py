import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("magenta")

def drawSq(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

size=20

for i in range (5):
    drawSq(alex,size)
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()
    size=size+20
    
wn.exitonclick()