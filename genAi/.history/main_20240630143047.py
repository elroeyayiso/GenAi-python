import turtle
import math

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed

# Colors for the gradient
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]


# Function to draw the spiral star pattern
def draw_spiral_star(size, turns, angle):
    for i in range(turns):
        pen.color(colors[i % len(colors)])
        pen.forward(size)
        pen.left(angle)
        size += 2  # Increase the size to create the spiral effect


# Initial settings
pen.penup()
pen.goto(0, 0)
pen.pendown()

# Draw the spiral star pattern
draw_spiral_star(10, 200, 144)  # Adjust the parameters for different effects

# Finish up
pen.hideturtle()
turtle.done()
