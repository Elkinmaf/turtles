import turtle

import random

riley = turtle.Turtle()

possible_moods= ["party", "happy", "quiet", "angry", "sad"]

mood = random.choice(possible_moods)

riley.width(5)

if mood == "happy":
    riley.color("yellow")
else:
    if mood == "sad":
        riley.color("blue")
    else:
        if mood == "party":
            riley.color("cyan")
        else:
            if mood == "angry":
                riley.color("red")
            else:
                riley.color("gray")

# Best way to do:

# if mood == "happy":
#     riley.color("yellow")
# elif mood == "sad":
#     riley.color("blue")
# elif mood == "angry":
#     riley.color("red")
# elif mood == "party"
#     riley.color("cyan")
# else:
#     riley.color("gray")


for side in range(5):
    riley.forward(100)
    riley.right(144)