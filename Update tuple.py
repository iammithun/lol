# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:32:53 2023

@author: mithun sai
"""
#This codes created by mithun sai
#This codes is about Update tuple
#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
# apple, kiwi, banana, cherry
print(x)
#Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#-- orange apple, banana, cherry

print(thistuple)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#--apple, orange, banana, cherry
#Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#--banana cherry
