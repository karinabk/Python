#You are given a string and your task is to swap cases.
#In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    list_=list(s)
    for i in range(len(list_)):
        if ord(list_[i])>64 and ord(list_[i])<91:
            list_[i]=list_[i].lower()
        elif ord(list_[i])>96 and ord(list_[i])<123:
            list_[i]=list_[i].upper()
    return "".join(list_)
    
    
    #Now it works
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
