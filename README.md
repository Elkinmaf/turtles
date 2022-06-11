# turtles
Basic projects working with Python Turtle Module
The turtles will follow the indications from their own angle and perspective.
You can indicate go:

Forward
Right
Back
Left

But all having perspective of the turtle. The number indicated is related to pixels, and the angle in the case of right and left is related to degrees.

Loop can replace multiple lines of code in just 3. Example:

amy.forward(100)
amy.left(90)
amy.forward(100)
amy.left(90)
amy.forward(100)
amy.left(90)
amy.forward(100)
amy.left(90)

can be replaced for:

for side in [1, 2, 3, 4]:
    amy.forward(100)
    amy.left(90)

the numbers in the brackets actually don't matter and represent the quantity of elements. In this case, 4 so 4 times will happen the instructions forward and left.

It's possible to include changes in the loops:

for length in [10, 20, 30, 40, 50, 60]:
    dizzy.forward(length)
    length = 100
    dizzy.forward(length)

in this case the first time dizzy will move 110.

for length in [10, 20, 30, 40, 50, 60]:
    length = 100
    dizzy.forward(length)
    dizzy.right(90)

in this case, dizzy will always move 100, since the value is replaced before the next action in the loop takes part

A nested loop is a loop inside another one.

The polygons will have also 360 degrees, so for getting the right angle that the turtle needs to turn for creating it, you can divide 360 in the number of sides:
For example, in a pentagon, will be 360/5=72 degrees
square: 360/4= 90 degrees

A method is a function related to a specific object.
e.g mary.color("red")
There are other kind of functions that are not related to objects, like range(100)

edna.home() is a call to the method named home on an object named edna.

max(23, 17) is a call to the function named max.

print is not a call; it's something else. Specifically, it's just the name of a function.

