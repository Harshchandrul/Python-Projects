import turtle

# Create a screen object
screen = turtle.Screen()

# Set the tracer to 0 to turn off automatic screen updates
# screen.tracer(0)

# Create a turtle object
t = turtle.Turtle()
t.speed(speed='fastest')

# Draw a large number of lines
for i in range(1000):
    t.forward(i)
    t.right(89)

# Manually update the screen to display the drawing
screen.update()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
