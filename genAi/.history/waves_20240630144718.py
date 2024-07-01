import turtle
import math

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")

wave = turtle.Turtle()
wave.speed(0)  # Set the turtle's speed (0 is the fastest)

# Adjust these parameters to control the wave
amplitude = 50  # Height of the wave
frequency = 0.05  # Frequency of the wave
length = 600  # Length of the wave


# Function to draw a smooth wave
def draw_wave():
    wave.penup()
    wave.goto(-length / 2, 0)  # Start from the left edge of the screen
    wave.pendown()

    for x in range(-int(length / 2), int(length / 2)):
        y = amplitude * math.sin(frequency * x)
        wave.goto(x, y)

    wave.hideturtle()


# Draw the wave
draw_wave()

# Keep the window open until it's closed by the user
turtle.done()
