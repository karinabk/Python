#You are given a string S
#Your task is to find out if the string 
#contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters. 

if __name__ == '__main__':
    s = input()
    list_=str(s.split())
    for i in list_:
        alpha= False
        alpha = i.isalpha()
        if alpha == True:
            break
    for i in list_:
        num= False
        num=i.isdigit()
        if num == True:
            break
    for i in list_:
        low = False
        low=i.islower()
        if low == True:
            break
    for i in list_:
        up=False
        up=i.isupper()
        if up == True:
            break
            
    alnum = True if alpha or num else False
            
    print(alnum)
    print(alpha)
    print(num)
    print(low)
    print(up)
    
        
