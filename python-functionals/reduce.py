'''First line contains n, the number of rational numbers. 
The i_th of next n lines contain two integers each, the numerator( N_i ) and denominator( D_i ) of the i_th rational number in the list.

Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than 1'''

from fractions import Fraction
from functools import reduce
from fractions import gcd
def product(fracs):
    t = reduce(lambda x,y: x*y, fracs)
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
