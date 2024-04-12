import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Create a turtle object
galaxy = turtle.Turtle()
galaxy.speed(0)  # Set the fastest drawing speed

# Function to draw a star
def draw_star(x, y, size, color):
    galaxy.penup()
    galaxy.goto(x, y)
    galaxy.pendown()
    galaxy.color(color)
    galaxy.begin_fill()
    galaxy.circle(size)
    galaxy.end_fill()

# Function to draw the galaxy
def draw_galaxy(num_stars):
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.uniform(0.1, 2.0)
        brightness = random.randint(100, 255)
        color = "#%02x%02x%02x" % (brightness, brightness, brightness)
        draw_star(x, y, size, color)

# Draw the galaxy
draw_galaxy(300)

# Hide the turtle and display the result
galaxy.hideturtle()
screen.mainloop()
