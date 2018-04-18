'''Task
You are given a space separated list of integers. 
If all the integers are positive, then you need to check if any integer is a palindromic integer.'''





#Can you solve this challenge in 3 lines of code or less?


N=int(input())
num=list(map(int,input().split()))
print(all([i>0 for i in num]) and any([i==int("".join(reversed(str(i)))) for i in num]))
