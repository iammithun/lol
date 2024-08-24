# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:34:22 2024

@author: iamrs
"""

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Rainbow colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# Draw the infinity symbol with rainbow colors
for i in range(360):
    t.pensize(2)
    t.color(colors[i % len(colors)])
    t.forward(1)
    t.left(1)

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()
