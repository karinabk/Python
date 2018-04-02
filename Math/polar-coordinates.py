#Task 
#You are given a complex z. Your task is to convert it to polar coordinates.
#Output Format
#Output two lines: 
#The first line should contain the value of modulus. 
#The second line should contain the value of phase angle.


import cmath
if __name__ == '__main__':
    n = complex(input())
    print(abs(n))
    print(cmath.phase(n))
