import turtle 
wn=turtle.Screen()
t=turtle.Turtle()
t.speed(10)

def drawFivePointStar(t,n):
    for i in range(n):
        t.forward(100)
        t.left(180 - 180/n)


drawFivePointStar(t,9)