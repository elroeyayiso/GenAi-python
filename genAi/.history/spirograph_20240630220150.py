import turtle


# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("")
pen.width(1)


# Function to draw a spirograph-like pattern
def draw_spirograph(radius, angle, steps, repeats):
    for i in range(repeats):
        for j in range(steps):
            pen.forward(radius)
            pen.right(angle)
        pen.right(360 / repeats)


# Parameters for the spirograph
radius = 100  # Distance to move forward
angle = 144  # Angle to turn
steps = 200  # Number of steps in each repetition
repeats = 36  # Number of repetitions to create the full pattern

# Draw the pattern
pen.penup()
pen.goto(0, 0)
pen.pendown()
draw_spirograph(radius, angle, steps, repeats)

# Finish up
pen.hideturtle()
turtle.done()
