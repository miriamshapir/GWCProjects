from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
color=input('What color do you want?')
t.pencolor(color)
sides=int(input('How many sides do you want?'))
t.pendown
for square in range(sides):
    t.fd(60)
    t.rt(360/sides)






# Close window on click.
exitonclick()
