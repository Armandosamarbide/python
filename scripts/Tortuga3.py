import turtle

pantalla=turtle.Screen()
pantalla.bgcolor('black')
turtle.getscreen()

# Inicializamos la posición de la tortuga.

turtle.hideturtle()
turtle.penup()
turtle.goto(-200,-100)
turtle.pendown()
turtle.showturtle()

# Inicializamos colores y tamaños

turtle.shape("classic")
turtle.shapesize(2, 2, 4)
turtle.width(3)
turtle.color('white','purple')

# Dibujamos la figura

turtle.speed(8)
turtle.begin_fill()
for i in range (8):
    turtle.forward(500)
    turtle.left(135)
turtle.end_fill()

turtle.hideturtle()

turtle.mainloop()