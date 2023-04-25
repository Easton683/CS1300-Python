'''Old Glory Creator'''

# -------------------
# DOCTYPE Python
# Easton Jackson CS 1300
# Coding Ten
# 4/18/2023
# -------------------

import turtle

# Set up the turtle
t = turtle.Turtle()

# Set turtle to fastest speed
t.speed(0)

# Set up the variables for the flag
# Pulled some dimmensions from external website because 713 height messed up the dimmensions.
# https://www.ushistory.org/betsy/flagetiq3.html
HEIGHT = 300
WIDTH = 1.9 * HEIGHT
STRIPE_HEIGHT = HEIGHT / 13
CANTON_WIDTH = 0.76 * HEIGHT
CANTON_HEIGHT = 0.5385 * HEIGHT


def draw_rectangle(x, y, width, height, color):
    '''Function to draw a rectangle'''
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    rectangle_iterator = 0

    # looping for the sides
    while rectangle_iterator < 2:
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        rectangle_iterator = rectangle_iterator+1
    t.end_fill()


def main(width, height, canton_height, stripe_height):
    '''Main method to draw stripes and call other methods'''
# Draw the stripes
    stripe_iterator = 0
    while stripe_iterator < 13:
        if stripe_iterator % 2 == 0:
            stripe_color = "red"
        else:
            stripe_color = "white"
        draw_rectangle(-width/2, canton_height+height/2 - stripe_iterator *
                       stripe_height, width, stripe_height, stripe_color)
        stripe_iterator += 1

    # Draw the canton
    draw_rectangle(-WIDTH/2, HEIGHT/2, CANTON_WIDTH, -CANTON_HEIGHT, "blue")


# Calling main method
main(WIDTH, HEIGHT, CANTON_HEIGHT, STRIPE_HEIGHT)

# Hide the turtle
t.hideturtle()

# This program was very fun to make and turtle is very easy to use.
# Although I did not draw the stars,
# I learned a lot about how turtle functions and how we can draw certain things using turtle
