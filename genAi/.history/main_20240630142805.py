import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.color("green")
pen.speed(0)  # Fastest drawing speed


# Function to draw a fractal tree
def draw_fractal_tree(branch_length, pen):
    if branch_length > 5:  # Base case: stop when the branch is too small
        pen.forward(branch_length)
        pen.right(20)  # Turn right to draw the right subtree
        draw_fractal_tree(branch_length - 15, pen)
        
        pen.left(40)  # Turn left to draw the left subtree
        draw_fractal_tree(branch_length - 15, pen)
        
        pen.right(20)  # Turn back to the original direction
        pen.backward(branch_length)


# Initial settings
pen.left(90)  # Point the turtle upwards
pen.up()
pen.backward(100)
pen.down()
pen.color("brown")

# Draw the fractal tree
draw_fractal_tree(100, pen)

# Finish up
turtle.done()
