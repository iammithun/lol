# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:22:40 2024

@author: iamrs
"""

from turtle import Turtle, Screen

tim=Turtle()
scre=Screen()
scre.setup(width=800, height=400)
user_bet=scre.textinput(title="make your bet",prompt="Which turtle will win the race?. Enter the color of the turtle")

tim=Turtle()
tim.goto(x=-250, y=-100)

scre.exitonclick()