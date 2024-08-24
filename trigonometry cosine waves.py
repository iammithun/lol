# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:11:59 2024

@author: iamrs
"""

import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Cosine Wave with Turtle Graphics")

# Create a turtle named "cosine"
cosine = turtle.Turtle()
cosine.speed(0)
cosine.penup()

# Move the turtle to the starting point
cosine.goto(-360, 0)
cosine.pendown()

# Draw the cosine wave
for x in range(-360, 361):
    y = 100 * math.cos(math.radians(x))
    cosine.goto(x, y)

# Hide the turtle
cosine.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
