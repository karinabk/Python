#In this challenge, the user enters a string and a substring. 
#You have to print the number of times that the substring occurs in the given string.
#String traversal will take place from left to right, not from right to left. 

def count_substring(string, sub_string):
    count =0
    for i in range(len(string)):
        if string[i]==sub_string[0]:
            for k in range(len(sub_string)):
                if string[i+k-1]!=sub_string[k]:
                    break
                if k==len(sub_string)-1:
                    count+=1
        
    
    return count
    
    
    #DOES NOT WORK YET

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
