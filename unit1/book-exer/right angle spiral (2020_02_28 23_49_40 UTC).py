import turtle
wn=turtle.Screen()
leo=turtle.Turtle()
wn.bgcolor("lightgreen")
leo.color("blue")
leo.speed(10)

lgth=5

leo.left(180)

for i in range(40):
    leo.forward(lgth)
    leo.right(90)
    lgth=lgth+5
    leo.forward(lgth)
    leo.right(90)


wn.exitonclick()