#In this challenge, the user enters a string and a substring. 
#You have to print the number of times that the substring occurs in the given string.
#String traversal will take place from left to right, not from right to left. 

def count_substring(string, sub_string):
    count =0
    string=list(string)
    sub_string=list(sub_string)
    for i in range(len(string)):
        if string[i]==sub_string[0]: # finds beginning of the sub string
            for k in range(len(sub_string)):
                if k+1==len(sub_string): # counts amount of sub strings 
                    count+=1
                    break
                if i+1==len(string): # in case if it is the end of the string
                    break
                if string[i+1]!=sub_string[k+1]: # in case if it is the end of the sub string
                    break
                i+=1 # iteration of string index
        if i+1==len(string):
            break
    return count
    
    
    #IT WORKS NOW ( FINALLLYYYYYY)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
