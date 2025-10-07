import turtle

turtle.getscreen()
turtle.shape("turtle")
turtle.shapesize(1,1,1)

print(turtle.xcor())
print(turtle.ycor())

turtle.color("black","red")
turtle.pencolor("black")
turtle.pensize(3)
turtle.begin_fill()
for i in range (8):
    turtle.forward(500)
    turtle.left(135)
turtle.end_fill()
turtle.mainloop()