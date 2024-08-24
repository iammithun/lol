# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:21:37 2024

@author: iamrs
"""

import turtle

# Create a Turtle object
pen = turtle.Turtle()

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

# Set the speed of the turtle
pen.speed(13232)  # You can adjust the speed as needed

# Set the size of the star
star_size = 100

# Call the function to draw the star
draw_star(star_size)

# Keep the window open until it's closed by the user
turtle.mainloop()
