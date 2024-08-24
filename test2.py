# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 11:19:19 2023

@author: iamrs
"""

import random
import pandas as pd
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

index  = count()

plt.style.use('fivethirtyeight')
x_vals = []
y_vals = []

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))    
    plt.plot(x_vals,y_vals)
    
ani = FuncAnimation(plt.gcf, animate, interval=1000)    
plt.plot(x_vals,y_vals)
plt.tight_layout()
plt.show()