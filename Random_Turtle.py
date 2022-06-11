import turtle
import random

colors=["red", "orange", "yellow", "green", "blue", "purple", "cyan"]

def random_angle():
    return random.randint(-360, 360)

def random_color():
    return random.choice(colors)

t = turtle.Turtle()
t.width(20)

for step in range(100):

    angle= random_angle()

    color = random_color()

    # Other options for the previous randoms:
    # angle = random.randint(-360, 360)
    # color = random.choice(colors)

    t.color(color)
    t.right(angle)
    t.forward(10)