import turtle
import random

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed
pen.width(2)  # Thicker lines for better visibility

# Colors



# Function to draw a spiral star pattern
def draw_spiral_star(size, turns, angle, increment):
    for i in range(turns):
        pen.color(colors[i % len(colors)])
        pen.forward(size)
        pen.left(angle)
        size += increment  # Increase the size to create the spiral effect


# Function to draw generative art
def generative_art():
    for _ in range(10):
        pen.penup()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        pen.goto(x, y)
        pen.pendown()
        size = random.randint(10, 20)
        turns = random.randint(50, 100)
        angle = random.randint(120, 150)
        increment = random.uniform(1, 3)
        draw_spiral_star(size, turns, angle, increment)


# Draw the generative art
generative_art()

# Finish up
pen.hideturtle()
turtle.done()
