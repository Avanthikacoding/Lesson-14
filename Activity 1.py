import turtle 
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,200)
polygon = turtle.Turtle()

num_sides = 5
side_length = 85
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
polygon.penup() 
polygon.goto(10,50)
polygon.pendown()
n = 4
for i in range(n):
    polygon.forward(50)
    polygon.right(90)
turtle.done()