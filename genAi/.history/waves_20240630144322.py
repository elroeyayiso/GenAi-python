import turtle
import numpy as np

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(1)
pen.hideturtle()

# Generate sample data
x = np.linspace(0, 10, 100)
num_lines = 30
y_offsets = np.linspace(-10, 10, num_lines)

# Define colors
colors = ["#0066ff", "#0099ff", "#00ccff", "#00ffff", "#00ffcc", "#00ff99",
          "#00ff66", "#00ff33", "#00ff00"]

# Plot multiple lines
for i, offset in enumerate(y_offsets):
    y = np.sin(x) + offset  # Example data, you can customize this
    pen.penup()
    pen.goto(-300, y[0] * 20)  # Adjusting the initial position of the turtle
    
    pen.pendown()
    pen.color(colors[i % len(colors)])
    for j in range(1, len(x)):
        pen.goto(-300 + (x[j] * 60), y[j] * 20)

# Finish up
turtle.done()
