'''ABC is a right triangle, 90 degrees at B.
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC. 
Your task is to find angle MBC in degrees.'''


import math as m
x= int(input())
y=int(input())
deg_sym = '\xB0'                                              #for degree symbol
median = m.sqrt((x*x+y*y)/4+y*y-y*y)                          #findning median by law of cosines
angle=m.acos((median*median+y*y-(x*x+y*y)/4)/(2*median*y))    #finding angle by the same law

print(str(round(m.degrees(angle)))+deg_sym)
