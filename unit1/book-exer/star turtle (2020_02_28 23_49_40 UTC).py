import turtle

def drawLine(length, angle):
    mike=turtle.Turtle()
    mike.left(angle)
    mike.forward(length/2)
    mike.forward(-length)
    mike.forward(length/2)

def star(nlines):
    for angle in range(0, 180, int(360/nlines)):
        drawLine(200, angle)

star(8)