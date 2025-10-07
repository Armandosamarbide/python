import turtle

t = turtle.Turtle()

pantalla=turtle.Screen()
pantalla.bgcolor('white')
turtle.getscreen()

t.penup()
t.goto(0, -100)
t.pendown()

t.shape('classic')
t.shapesize(2,2,2)
t.width(6)
t.fillcolor()
t.color('black','purple')

t.begin_fill()
for i in range (8):
    t.forward(400)
    t.left(135)

t.end_fill()

t.mainloop()

