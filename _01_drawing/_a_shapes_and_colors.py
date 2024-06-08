import turtle


window = turtle.Screen()
window.bgcolor('purple')

# This code makes a new Turtle. Pick a new name for the turtle
my_turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
my_turtle.shape('turtle')
# Set your turtle's speed using .speed(2)
my_turtle.color('white')
# Set your turtle's color using .color('green') and .pencolor('blue')
my_turtle.speed(10)
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
my_turtle.forward(200)
# Move your turtle left or right using .left(90) or .right(90)
my_turtle.left(95)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
for num in range(90):
    my_turtle.forward(200)
    my_turtle.left(95)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
my_turtle.goto(50,0)
my_turtle.goto(0,50)
my_turtle.goto(100,0)
my_turtle.goto(0,100)
my_turtle.goto(150,0)
my_turtle.goto(0,150)
my_turtle.goto(200,0)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
my_turtle.circle(100, 360)
my_turtle.circle(110, 360)
my_turtle.circle(120, 360)
my_turtle.circle(130, 360)
my_turtle.circle(140, 360)
my_turtle.circle(150, 360)
my_turtle.circle(160, 360)
my_turtle.circle(170, 360)
my_turtle.circle(180, 360)
my_turtle.circle(190, 360)
my_turtle.circle(200, 360)
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
