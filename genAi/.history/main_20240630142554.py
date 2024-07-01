import turtle

# Set up the turtle
screen = turtle.Screen()
pen = turtle.Turtle()


# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90) 
        


# Draw a square with side length 100
draw_square(100)

# Finish up
turtle.done()
