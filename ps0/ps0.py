# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:10:16 2019

@author: David House
"""
import numpy

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
x_to_the_y = x**y
print("x**y = "+ str(x_to_the_y) )
log_2_x = numpy.log2(x)
print("log(x) = " + str(log_2_x))

