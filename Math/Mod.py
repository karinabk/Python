#Task 
#Read in two integers, a and b, and print three lines. 
#The first line is the integer division a//b 
#The second line is the result of the modulo operator: a%b. 
#The third line prints the divmod of a and b. 

if __name__ =='__main__':
    n = int(input())
    m = int(input())
    print(n//m)
    print(n%m)
    print(divmod(n,m))
