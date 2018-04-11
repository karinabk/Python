'''Task 
You are given two arrays (A & B) of dimensions N X M. 
Your task is to perform the following operations:
Add (A+B) 
Subtract (A-B) 
Multiply (A*B) 
Divide (A/B) 
Mod (A%B) 
Power (A**B)
'''


import numpy
n, m = map(int, input().split())
a, b = (numpy.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
