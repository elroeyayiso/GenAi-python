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
num_waves = 3  # Number of waves to repeat


# Function to draw a smooth wave with multiple colors
def draw_wave():
    for wave_num in range(num_waves):
        wave.penup()
        wave.goto(-length / 2, -amplitude * wave_num * 2)
        wave.pendown()

        for x in range(-int(length / 2), int(length / 2)):
            color = get_color(x)  # Get color based on x position
            wave.color(color)
            y = amplitude * math.sin(frequency * x)
            wave.goto(x, y - amplitude * wave_num * 2)

    wave.hideturtle()


# Function to determine color based on position
def get_color(x):
    if x < -length / 4:
        return "blue"
    elif x < 0:
        return "green"
    elif x < length / 4:
        return "orange"
    else:
        return "red"


# Draw the repeating wave pattern
draw_wave()

# Keep the window open until it's closed by the user
turtle.done()