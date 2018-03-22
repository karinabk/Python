#You are given a string and your task is to swap cases.
#In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    list_=list(s)
    for i in list_:
        if ord(i)>64 and ord(i)<91:
            i= ord(i)+(97-65)
        elif ord(i)>96 and ord(i)<123:
            i=ord(i)-(97-65)
    string=str(list_)
    
    "".join(string)
    return string
    
    
    #DOES NOT WORK YET
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
