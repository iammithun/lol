# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:39:06 2023

@author: iamrs
"""




menu = ["Idly", "Dosa", "Sambar Rice", "Poori", "Chapati"]


mithuns_coco = ["Dosa", "Poori", "Biryani", "Chapati"]
for menu in menu:
   print(menu)
   for coco in mithuns_coco:
     if coco in menu:
        print(f"{coco} is available. Server: Please serve {coco} to the table.")
       
else:
        print(f"Sorry, {coco} is not available in our menu. Server: Please choose something else.")