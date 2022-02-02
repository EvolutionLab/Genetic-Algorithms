# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:02:02 2022

@author: plate
"""

import math

class Circle:
    def __init__(self, radius):
        
        self.radius = radius
    
    def get_area(self):
        
        return math.pi*self.radius*self.radius


for i in range(1, 10):
    
    if i ==0:
        
        continue
    
    circle = Circle(i)
    
    print('A circle with radius {0} has area {1:0.3f}'.format(i, circle.get_area()))
    

































