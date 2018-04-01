#Task 
#You are given three integers: a, b, and m, respectively. Print two lines. 
#The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m). 

if __name__=='__main__':
    number = int(input())
    power= int(input())
    mod_=int(input())
    print(pow(number,power))
    print(pow(number,power,mod_))
