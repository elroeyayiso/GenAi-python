import turtle
import random
import math


def draw_circle(t, x, y, radius, n_lines):
    for i in range(n_lines):
        angle_offset = random.uniform(0, 2 * math.pi)
        for angle in range(360):
            radian_angle = math.radians(angle) + angle_offset
            offset = random.uniform(-2, 2)
            t.goto(x + (radius + offset) * math.cos(radian_angle),
                   y + (radius + offset) * math.sin(radian_angle))
        radius += 10


def draw_pattern(t, width, height, num_circles):
    t.speed(0)
    t.hideturtle()
    for _ in range(num_circles):
        x = random.randint(-width // 2, width // 2)
        y = random.randint(-height // 2, height // 2)
        radius = random.randint(10, 30)
        n_lines = random.randint(5, 15)
        draw_circle(t, x, y, radius, n_lines)


def main():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor('black')
    t = turtle.Turtle()
    t.color('lightgreen')
    t.penup()
    t.goto(0, 0)
    t.pendown()

    draw_pattern(t, 800, 800, 10)

    screen.mainloop()


if __name__ == "__main__":
    main()
