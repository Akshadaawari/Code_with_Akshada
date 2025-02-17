import turtle

screen = turtle.Screen()
screen.bgcolor("black")  # Set background color (optional)

pen = turtle.Turtle()
pen.speed(1)  # Set drawing speed (0 is the fastest)
pen.color("pink")

pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.setheading(60)
pen.circle(-90,200)
pen.forward(180)
pen.end_fill()

pen.hideturtle() # Hide the turtle icon

turtle.done()