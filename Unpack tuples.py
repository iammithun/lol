# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:41:24 2023

@author: Mithun sai 
"""
#this codes is created by mithun sai
#this codes is about Unpack tuples
#Unpacking a Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

 
