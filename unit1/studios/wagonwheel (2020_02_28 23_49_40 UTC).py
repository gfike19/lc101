import turtle
wn = turtle.Screen()
raph = turtle.Turtle()
raph.speed(10)

def drawSq(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

for i in range (20):
    drawSq(raph,100)
    raph.right(18)
    raph.pendown()

wn.exitonclick()