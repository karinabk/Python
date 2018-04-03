#Using the distance formula and trigonometry functions in Python,
#calculate the magnitude and direction of a line with the two coordinates, (5,3) and (1,1).

import numpy as np
import math
coords1 = np.array([5,3])
coords2 = np.array([1,1])
magnitude = np.linalg.norm(coords1-coords2)
coords3=coords1-coords2
direction = np.arctan(coords3[1]/coords3[0])
#without numpy
coords1 = [5,3]
coords2 = [1,1]
coords3=[]
coords3.append(coords1[0]-coords2[0])
coords3.append(coords1[1]-coords2[1])
magnitude=(coords3[1]**2+coords3[0]**2)**(1/2)
