#2.2.1 Challenge
#   Write the representation of ℜ2 as a list comprehension - use ranges between -10 and 10 for all values of x and y.
#    Write the representation of ℜ3 as a list comprehension - use ranges between -10 and 10 for all values of x, y, and z.
#   Write a list comprehension that represents the the set V = {(x, y, z) | x, y, z ∈ ℜ and x+y = 11}. 
#Use ranges between -10 and 10 for all values of x, y, and z.





R2=np.array([])
x =0
y=0
R2 = [([x,y]) for y in range(-10,10) for x in range(-10,10)]
R3 = [([x,y,z]) for z in range(-10,10) for y in range(-10,10) for x in range(-10,10)]
V= [([x,y,z]) for z in range(-10,10) for y in range(-10,10) for x in range(-10,10) if x+y==11]
