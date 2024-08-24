# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:53:56 2024

@author: iamrs
"""
######## Challenge 1 - Draw a Square ############
import turtle as t

t.shape("turtle")
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("OrangeRed3")

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
