'''Task

Print the value of a/b. 
In the case of ZeroDivisionError or ValueError, print the error code.'''


N=int(input())

for i in range(N):
    num=list(map(str,input().split()))
    try:
        print(round(int(num[0])/int(num[1])))
    except ValueError:
        if num[0].isdigit():
            print("Error Code: invalid literal for int() with base 10: '{0}'".format(num[1]))
        else:
            print("Error Code: invalid literal for int() with base 10: '{0}'".format(num[0]))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
